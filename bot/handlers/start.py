import logging
from pyrogram import Client, filters
from bot import app


logging.basicConfig(level=logging.INFO)

@app.on_message(filters.private & filters.command("start"))  # Handle /start command
async def start_command(client, message):
    print("✅ Start command received!")  # Debugging step
    logging.info(f"📩 Received /start from {message.from_user.first_name}")
    await message.reply_text("👋 Hello! Welcome to the Pregnancy Tracker Bot!")
