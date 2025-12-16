
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

OWNER_ID = int(os.getenv("SUDO_USERS").split()[0])

SESSION_FILE = "session.txt"

STRING_SESSION = None
if os.path.exists(SESSION_FILE):
    with open(SESSION_FILE, "r") as f:
        STRING_SESSION = f.read().strip()
