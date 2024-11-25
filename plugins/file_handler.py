from pyrogram import Client, filters
from pyrogram.types import Message
import re

@Client.on_message(filters.command("genlink"))
async def generate_link(client, message: Message):
    if not message.reply_to_message:
        await message.reply_text("Please reply to a file to generate a link.")
        return

    file = message.reply_to_message

    if not hasattr(file, 'document') and not hasattr(file, 'video') and not hasattr(file, 'audio'):
        await message.reply_text("Please reply to a valid file.")
        return

    file_id = file.document.file_id if hasattr(file, 'document') else \
              file.video.file_id if hasattr(file, 'video') else \
              file.audio.file_id

    stored_file = await client.db.store_file(file_id, file.id, message.chat.id)
    link = f"https://t.me/{(await client.get_me()).username}?start=file_{stored_file.inserted_id}"
    
    await message.reply_text(f"Here's your file link:\n{link}")

@Client.on_message(filters.command("batch"))
async def batch_handler(client, message: Message):
    # Initial message
    await message.reply_text(
        "Forward The Batch First Message From your Batch Channel (With Forward Tag).. "
        "or Give Me Batch First Message link from your batch channel"
    )