from pyrogram import Client, filters
import random

PREGNANCY_TIPS = [
    "Stay hydrated! Drink at least 8 glasses of water daily. 💧",
    "Eat a balanced diet with plenty of fruits and vegetables. 🥦🍎",
    "Take prenatal vitamins as prescribed by your doctor. 💊",
    "Get enough sleep and rest whenever possible. 😴",
    "Exercise moderately, like walking or prenatal yoga. 🏃‍♀️",
]

async def tips_command(client, message):
    """Handles the /tips command to send a random pregnancy tip."""
    tip = random.choice(PREGNANCY_TIPS)
    await message.reply_text(f"📝 Pregnancy Tip:\n{tip}")

tips_handler = filters.command("tips") & filters.private
