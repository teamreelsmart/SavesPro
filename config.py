# ---------------------------------------------------
# File Name: Config.py
# Author: NeonAnurag
# GitHub: https://github.com/MyselfNeon/
# Telegram: https://t.me/MyelfNeon
# Created: 2025-11-21
# Last Modified: 2025-11-22
# Version: Latest
# License: MIT License
# ---------------------------------------------------

import os

# Bot Token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Port for Web Server
PORT = int(os.environ.get("PORT", "8080"))

# Your API ID & Hash
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "841851780"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "SaveRestricted")

# Log Channel to Track New Users 
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001889915480"))

# Dump Channel for File Tracking (ADDED)
DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", "-1002766188813"))

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then False
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))

# Keep-Alive URL
KEEP_ALIVE_URL = os.environ.get("KEEP_ALIVE_URL", "")

# Start pic on /start 
START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/krxuel.jpg")

# Force Subscribe Channel (set 0 to disable)
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL_URL = os.environ.get("FORCE_SUB_CHANNEL_URL", "https://t.me/your_channel")

# Optional UI Photos
VERIFY_PIC = os.environ.get("VERIFY_PIC", "")
MY_PLAN_PIC = os.environ.get("MY_PLAN_PIC", "")
FORCE_SUB_PIC = os.environ.get("FORCE_SUB_PIC", "")
BYPASS_ALERT_PIC = os.environ.get("BYPASS_ALERT_PIC", "")
AUTO_DELETE_SECONDS = int(os.environ.get("AUTO_DELETE_SECONDS", "0"))

# -------------------
# VERIFICATION CONFIG
# -------------------
VERIFY = bool(os.environ.get('VERIFY', True)) # Set True to enable
VERIFY_SHORTLINK_URL = os.environ.get('VERIFY_SHORTLINK_URL', 'ShrinkMe.io') # Your Shortener Domain
VERIFY_SHORTLINK_API = os.environ.get('VERIFY_SHORTLINK_API', '') # Your Shortener API Key
VERIFY_TUTORIAL = os.environ.get('VERIFY_TUTORIAL', 'https://t.me/your_tutorial_link') # Tutorial Link

VERIFY_MIN_SECONDS = int(os.environ.get("VERIFY_MIN_SECONDS", "180"))
VERIFY_BYPASS_BAN_ATTEMPTS = int(os.environ.get("VERIFY_BYPASS_BAN_ATTEMPTS", "2"))

# -------------------
# PREMIUM CONFIG
# -------------------
FREE_SAVE_COOLDOWN_SECONDS = int(os.environ.get("FREE_SAVE_COOLDOWN_SECONDS", "60"))
PRO_DAILY_BATCH_LIMIT = int(os.environ.get("PRO_DAILY_BATCH_LIMIT", "500"))

PREMIUM_OVERVIEW_TEXT = os.environ.get(
    "PREMIUM_OVERVIEW_TEXT",
    "<b>💎 Premium Plans</b>\n\n"
    "<b>PRO:</b> No cooldown, verification required, batch limit 500/day.\n"
    "<b>PRO GOLD:</b> No cooldown, no verification, unlimited batch."
)

PRO_PLAN_NAME = os.environ.get("PRO_PLAN_NAME", "PRO PLAN")
PRO_PLAN_QR_IMAGE = os.environ.get("PRO_PLAN_QR_IMAGE", "https://example.com/pro_qr.jpg")
PRO_PLAN_DETAILS = os.environ.get(
    "PRO_PLAN_DETAILS",
    "<b>✅ PRO Plan</b>\nNo cooldown\nBatch limit: 500/day\nVerification required"
)

PRO_GOLD_PLAN_NAME = os.environ.get("PRO_GOLD_PLAN_NAME", "PRO GOLD PLAN")
PRO_GOLD_PLAN_QR_IMAGE = os.environ.get("PRO_GOLD_PLAN_QR_IMAGE", "https://example.com/pro_gold_qr.jpg")
PRO_GOLD_PLAN_DETAILS = os.environ.get(
    "PRO_GOLD_PLAN_DETAILS",
    "👑 PRO GOLD PLAN – ₹200\n\n"
    "🔥 Uʟᴛɪᴍᴀᴛᴇ Pʀᴇᴍɪᴜᴍ Aᴄᴄᴇss:\n\n"
    "✅ Nᴏ Cᴏᴏʟᴅᴏᴡɴ Tɪᴍᴇ\n"
    "✅ Nᴏ Vᴇʀɪғɪᴄᴀᴛɪᴏɴ Rᴇǫᴜɪʀᴇᴅ\n"
    "✅ Uɴʟɪᴍɪᴛᴇᴅ Bᴀᴛᴄʜ Mᴇssᴀɢᴇ Sᴀᴠɪɴɢ\n"
    "✅ Fᴀsᴛᴇsᴛ Pʀᴏᴄᴇssɪɴɢ Sᴘᴇᴇᴅ\n"
    "✅ Fᴜʟʟ Bᴏᴛ Aᴄᴄᴇss\n"
    "✅ Pʀɪᴏʀɪᴛʏ Sᴜᴘᴘᴏʀᴛ\n\n"
    "💳 Pᴀʏᴍᴇɴᴛ Mᴇᴛʜᴏᴅ\n\n"
    "UPI ID: luciferjaat@ptyes\n"
    "Pᴀʏ ᴜsɪɴɢ UPI / GPᴀʏ / PʜᴏɴᴇPᴇ / Pᴀʏᴛᴍ\n\n"
    "📌 Aғᴛᴇʀ Pᴀʏᴍᴇɴᴛ:\n"
    "Sᴇɴᴅ Pᴀʏᴍᴇɴᴛ Sᴄʀᴇᴇɴsʜᴏᴛ ᴛᴏ Aᴅᴍɪɴ ғᴏʀ Iɴsᴛᴀɴᴛ Aᴄᴛɪᴠᴀᴛɪᴏɴ."
)

PREMIUM_CONTACT_BUTTON_TEXT = os.environ.get("PREMIUM_CONTACT_BUTTON_TEXT", "📞 Contact Admin")
PREMIUM_CONTACT_URL = os.environ.get("PREMIUM_CONTACT_URL", "https://t.me/your_admin_username")


# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
