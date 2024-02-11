import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "26724473").strip()
API_HASH = os.getenv("API_HASH", "7bc7d1f9b2f3d3f1bfd272db56ac0ba1").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6949687629:AAGLAOCxgr0Z30cYZldqKvVjD-SP_AO4eRM").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://igzvmvzd:4G6i3O51PB9ZBSO0RcArUlcBBoWMv-es@bubble.db.elephantsql.com/igzvmvzd").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "@SpotifyStreamMusic")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
