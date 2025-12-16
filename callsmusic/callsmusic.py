from pyrogram import Client
from pytgcalls import PyTgCalls

import config
from . import queues

# -----------------------
# BOT CLIENT (always on)
# -----------------------
bot = Client(
    "bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# -----------------------
# USER CLIENT (optional)
# -----------------------
user = None
pytgcalls = None


def start_userbot():
    """
    Starts user session + PyTgCalls
    Called only if STRING_SESSION exists
    """
    global user, pytgcalls

    if not config.STRING_SESSION:
        print(">> No STRING_SESSION found. Userbot not started.")
        return

    print(">> Starting userbot session...")

    user = Client(
        session_string=config.STRING_SESSION,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        in_memory=True
    )

    user.start()

    pytgcalls = PyTgCalls(user)

    @pytgcalls.on_stream_end()
    def on_stream_end(chat_id: int):
        queues.task_done(chat_id)

        if queues.is_empty(chat_id):
            pytgcalls.leave_group_call(chat_id)
        else:
            pytgcalls.change_stream(
                chat_id,
                queues.get(chat_id)["file"]
            )

    pytgcalls.start()
    print(">> Userbot + PyTgCalls started successfully.")


# -----------------------
# Expose run method safely
# -----------------------
def run():
    if pytgcalls:
        pytgcalls.run()
