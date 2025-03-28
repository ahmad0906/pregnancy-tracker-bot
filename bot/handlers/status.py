from pyrogram import Client, filters
from database import get_pregnancy_data
from utils.date_calculations import get_pregnancy_week

async def status_command(client, message):
    """Handles /status command to check pregnancy status."""
    user_id = message.from_user.id
    user_data = get_pregnancy_data(user_id)

    if not user_data:
        await message.reply_text("❌ You haven't started tracking yet! Send your LMP date in `YYYY-MM-DD` format.")
        return

    lmp_date = user_data["lmp"]
    due_date = user_data["due_date"]
    weeks_pregnant = get_pregnancy_week(lmp_date)

    await message.reply_text(
        f"📌 *Pregnancy Status:*\n"
        f"📅 LMP: `{lmp_date}`\n"
        f"🍼 Due Date: `{due_date}`\n"
        f"🗓️ Current Week: *{weeks_pregnant}*"
    )

status_handler = filters.command("status") & filters.private
