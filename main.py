import os
os.environ["TZ"] = "UTC"

from pyrogram import Client as Bot
from config import API_ID, API_HASH, BOT_TOKEN
from callsmusic.callsmusic import start_userbot

bot = Bot(
    "bot_session",          # <-- FILE BASED SESSION (IMPORTANT)
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

bot.start()

# start userbot only if session exists
start_userbot()

print(">> Bot started successfully.")
