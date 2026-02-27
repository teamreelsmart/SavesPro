from datetime import timezone
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    ADMINS, PREMIUM_OVERVIEW_TEXT, PRO_PLAN_NAME, PRO_PLAN_QR_IMAGE, PRO_PLAN_DETAILS,
    PRO_GOLD_PLAN_NAME, PRO_GOLD_PLAN_QR_IMAGE, PRO_GOLD_PLAN_DETAILS,
    PREMIUM_CONTACT_BUTTON_TEXT, PREMIUM_CONTACT_URL
)
from database.db import db


def premium_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ Pro Plan", callback_data="plan_pro"),
            InlineKeyboardButton("👑 Pro Gold", callback_data="plan_pro_gold")
        ],
        [InlineKeyboardButton("⬅️ Back", callback_data="start_btn")]
    ])


@Client.on_message(filters.command(["premium"]) & filters.private)
async def premium_command(client, message):
    await message.reply_text(PREMIUM_OVERVIEW_TEXT, reply_markup=premium_keyboard(), disable_web_page_preview=True)


@Client.on_message(filters.command(["add_premium_pro", "add_premium_gold"]) & filters.private)
async def add_premium(client, message):
    if message.from_user.id != ADMINS:
        return await message.reply_text("❌ Only admin can use this command.")

    if len(message.command) != 3:
        cmd = message.command[0]
        return await message.reply_text(f"Usage: /{cmd} <userid> <days>")

    try:
        user_id = int(message.command[1])
        days = int(message.command[2])
    except ValueError:
        return await message.reply_text("❌ userid and days must be numbers.")

    tier = "pro" if message.command[0] == "add_premium_pro" else "pro_gold"
    expires_at = await db.set_premium(user_id, tier, days)
    expiry_text = expires_at.astimezone(timezone.utc).strftime("%d %b %Y, %H:%M UTC")

    await message.reply_text(f"✅ {tier.upper()} activated for `{user_id}` till {expiry_text}.")

    try:
        await client.send_message(
            user_id,
            f"🎉 Your <b>{tier.upper()}</b> plan is now active.\n"
            f"Expiry: <b>{expiry_text}</b>\n\n"
            "Plan expiry ke baad account automatically FREE ho jayega."
        )
    except Exception:
        pass


@Client.on_callback_query(filters.regex("^premium_btn$"))
async def premium_btn(client, query):
    await query.message.edit_text(PREMIUM_OVERVIEW_TEXT, reply_markup=premium_keyboard(), disable_web_page_preview=True)
    await query.answer()


@Client.on_callback_query(filters.regex("^plan_pro$"))
async def pro_btn(client, query):
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton(PREMIUM_CONTACT_BUTTON_TEXT, url=PREMIUM_CONTACT_URL)],
        [InlineKeyboardButton("⬅️ Back To Plans", callback_data="premium_btn")]
    ])
    await client.send_photo(
        chat_id=query.message.chat.id,
        photo=PRO_PLAN_QR_IMAGE,
        caption=f"<b>{PRO_PLAN_NAME}</b>\n\n{PRO_PLAN_DETAILS}",
        reply_markup=kb
    )
    await query.answer()


@Client.on_callback_query(filters.regex("^plan_pro_gold$"))
async def gold_btn(client, query):
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton(PREMIUM_CONTACT_BUTTON_TEXT, url=PREMIUM_CONTACT_URL)],
        [InlineKeyboardButton("⬅️ Back To Plans", callback_data="premium_btn")]
    ])
    await client.send_photo(
        chat_id=query.message.chat.id,
        photo=PRO_GOLD_PLAN_QR_IMAGE,
        caption=f"<b>{PRO_GOLD_PLAN_NAME}</b>\n\n{PRO_GOLD_PLAN_DETAILS}",
        reply_markup=kb
    )
    await query.answer()
