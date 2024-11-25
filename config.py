from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = getenv("BOT_TOKEN")
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    ADMIN_IDS = [int(id.strip()) for id in getenv("ADMIN_ID").split()]
    MONGODB_URI = getenv("MONGODB_URI")
    DB_NAME = getenv("DB_NAME")
    PORT = int(getenv("PORT", "8080"))