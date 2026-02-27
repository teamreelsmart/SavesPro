# ---------------------------------------------------
# File Name: Verify.py
# ---------------------------------------------------

import logging
import random
import string
import aiohttp
from datetime import datetime, timedelta, timezone
from shortzy import Shortzy
from config import (
    VERIFY_SHORTLINK_URL, VERIFY_SHORTLINK_API, VERIFY, LOG_CHANNEL, ADMINS,
    VERIFY_MIN_SECONDS, VERIFY_BYPASS_BAN_ATTEMPTS
)
from database.db import db


async def get_verify_shorted_link(link):
    if VERIFY_SHORTLINK_URL == "api.shareus.io":
        url = f'https://{VERIFY_SHORTLINK_URL}/easy_api'
        params = {"key": VERIFY_SHORTLINK_API, "link": link}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                    return await response.text()
        except Exception as e:
            logging.error(f"Shortener Error: {e}")
            return link

    try:
        shortzy = Shortzy(api_key=VERIFY_SHORTLINK_API, base_site=VERIFY_SHORTLINK_URL)
        return await shortzy.convert(link)
    except Exception as e:
        logging.error(f"Shortzy Error: {e}")
        return link


async def get_token(bot, user_id, start_link):
    if not await db.is_user_exist(user_id):
        user = await bot.get_users(user_id)
        await db.add_user(user_id, user.first_name, user.username)

    token = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
    await db.update_verify_token(user_id, token)
    link = f"{start_link}verify-{user_id}-{token}"
    return await get_verify_shorted_link(link)


async def check_token(user_id, token):
    stored_token = await db.get_verify_token(user_id)
    return bool(stored_token and stored_token == token)


async def process_verification_success(bot, user_id, token):
    now = datetime.now(timezone.utc)
    issued_at = await db.get_verify_issued_at(user_id)

    bypass_detected = False
    elapsed_seconds = None
    attempts = 0
    banned_now = False

    if issued_at:
        if issued_at.tzinfo is None:
            issued_at = issued_at.replace(tzinfo=timezone.utc)
        elapsed_seconds = int((now - issued_at).total_seconds())
        if elapsed_seconds < VERIFY_MIN_SECONDS:
            bypass_detected = True
            attempts = await db.increment_verify_bypass_attempt(user_id)
            if attempts >= VERIFY_BYPASS_BAN_ATTEMPTS:
                await db.set_ban_status(user_id, True)
                banned_now = True

    await db.update_verify_date(user_id, now)
    if not bypass_detected:
        await db.reset_verify_bypass_attempt(user_id)

    try:
        user = await bot.get_users(user_id)
        bot_info = await bot.get_me()
        if bypass_detected:
            elapsed = elapsed_seconds if elapsed_seconds is not None else -1
            await bot.send_message(
                LOG_CHANNEL,
                f"**⌬ #VERIFY_BYPASS ⚠️**\n"
                f"**┟ Bot:** __@{bot_info.username}__\n"
                f"**┟ User:** __{user.mention}__\n"
                f"**┟ User ID:** `{user.id}`\n"
                f"**┟ Completed In:** `{elapsed}s` (Min `{VERIFY_MIN_SECONDS}s`)\n"
                f"**┟ Attempts:** `{attempts}`\n"
                f"**┖ Banned:** `{'YES' if banned_now else 'NO'}`"
            )
        else:
            await bot.send_message(
                LOG_CHANNEL,
                f"**⌬ #VERIFIED ✅**\n"
                f"**┟ Bot:** __@{bot_info.username}__\n"
                f"**┟ User:** __{user.mention}__\n"
                f"**┟ User ID:** `{user.id}`\n"
                f"**┟ Date:** __{now.strftime('%d %B, %Y')}__\n"
                f"**┖ Time:** __{now.strftime('%I:%M %p')}__"
            )
    except Exception as e:
        print(f"Log Error: {e}")

    return {
        "bypass_detected": bypass_detected,
        "elapsed_seconds": elapsed_seconds,
        "attempts": attempts,
        "banned_now": banned_now
    }


async def check_verification(user_id):
    if user_id == ADMINS:
        return True

    if await db.is_banned(user_id):
        return False

    tier, _ = await db.get_active_tier(user_id)
    if tier == "pro_gold":
        return True

    if not VERIFY:
        return True

    verified_time = await db.get_verify_date(user_id)
    if verified_time and datetime.now() < verified_time.replace(tzinfo=None) + timedelta(hours=4):
        return True

    return False
