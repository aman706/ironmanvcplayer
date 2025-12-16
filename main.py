import os
os.environ["TZ"] = "UTC"

from callsmusic.callsmusic import bot, start_userbot

# Start bot client (BOT_TOKEN based)
bot.start()

# Start userbot + PyTgCalls only if STRING_SESSION exists
start_userbot()

print(">> Bot is running and ready.")
