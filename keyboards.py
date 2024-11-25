from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("❓ Help", callback_data="help"),
         InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [InlineKeyboardButton("🤖 CREATE MY OWN CLONE", callback_data="clone")],
        [InlineKeyboardButton("📢 Update Channel", url="https://t.me/your_update_channel")]
    ])

def back_button():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("⬅️ Back", callback_data="back_main")
    ]])

def clone_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Clone", callback_data="add_clone")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back_main")]
    ])