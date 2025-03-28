import logging
from .config import API_ID, API_HASH, BOT_TOKEN
from pyrogram import Client

# Enable logging
logging.basicConfig(level=logging.INFO)

# Initialize the bot client
app = Client("pregnancy_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Import handlers
from .handlers import start, tips  # Ensure this line is included!

# Start the bot

print("✅ Bot is running and listening for messages...")
