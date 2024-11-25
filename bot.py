from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from config import Config
from database import Database
from keyboards import main_menu_keyboard, back_button, clone_menu_keyboard
import re

class FileStoreBot(Client):
    def __init__(self):
        super().__init__(
            name="FileStoreBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="plugins")
        )
        self.db = Database()

    async def start(self):
        await super().start()
        print("Bot started!")

    async def stop(self):
        await super().stop()
        print("Bot stopped!")

app = FileStoreBot()

@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    await client.db.add_user(message.from_user.id, message.from_user.username)
    welcome_text = """🚀 Build Your Own File Store Bot with @juststoreitbot

No coding needed! Get a powerful, feature-packed bot to store, share, and manage your files with ease. From custom access controls and batch uploads to real-time stats and 24/7 availability—this bot has it all.

Need more? You can even request additional features to make it truly your own!

👉 Click here to read the full list of features and get started!"""
    
    await message.reply_text(welcome_text, reply_markup=main_menu_keyboard())

@app.on_callback_query()
async def callback_handler(client, callback_query: CallbackQuery):
    if callback_query.data == "help":
        help_text = """✨ Help Menu

I am a permanent file store bot. You can store files from your public channel without me being admin in there. If your channel or group is private, first make me admin in there. Then you can store your files using the commands below and access stored files using the shareable link given by me.

📚 Available Commands:
➛ /start - Check if I am alive
➛ /genlink - To store a single message or file
➛ /batch - To store multiple messages from a channel
➛ /custom_batch - To store multiple random messages
➛ /shortener - To shorten any shareable links
➛ /settings - Customize your settings as needed
➛ /broadcast - Broadcast messages to users (moderators only)
➛ /ban - Ban a user (moderators only)
➛ /unban - Unban a user (moderators only)"""
        
        await callback_query.message.edit_text(help_text, reply_markup=back_button())

    elif callback_query.data == "about":
        about_text = """✨ ᴀʙᴏᴜᴛ ᴍᴇ

✰ ᴍʏ ɴᴀᴍᴇ: ꜰɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ
✰ ᴍʏ ᴏᴡɴᴇʀ: Crazy Devloper
✰ ᴜᴘᴅᴀᴛᴇs: Crazy
✰ sᴜᴘᴘᴏʀᴛ: Crazy
✰ ᴠᴇʀsɪᴏɴ: 0.7.9"""
        
        await callback_query.message.edit_text(about_text, reply_markup=back_button())

    elif callback_query.data == "clone":
        clone_text = """✨ Manage Clone's

You can now manage and create your very own identical clone bot, mirroring all my awesome features, using the given buttons."""
        
        await callback_query.message.edit_text(clone_text, reply_markup=clone_menu_keyboard())

    elif callback_query.data == "add_clone":
        instructions = """1) Create a bot using @BotFather
2) Then you will get a message with bot token
3) Send that bot token to me"""
        
        await callback_query.message.edit_text(instructions, reply_markup=back_button())

    elif callback_query.data == "back_main":
        await callback_query.message.edit_text(
            "Welcome back to the main menu!",
            reply_markup=main_menu_keyboard()
        )