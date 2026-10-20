from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

from config import CHANNEL_URL

# --- Foydalanuvchi tugmalari ---
BTN_ABOUT = "🔧 Karburator haqida"
BTN_ADDR = "📍 Ustaxona manzili"
BTN_PRICE = "💰 Barcha narxlar"
BTN_TIME = "🕒 Ish vaqti"

# --- Admin tugmalari ---
BTN_STATS = "📊 Statistika"
BTN_BROADCAST = "📢 Xabar yuborish"
BTN_EXIT = "⬅️ Chiqish"
BTN_CANCEL = "❌ Bekor qilish"


def main_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=BTN_ABOUT)],
            [KeyboardButton(text=BTN_ADDR), KeyboardButton(text=BTN_PRICE)],
            [KeyboardButton(text=BTN_TIME)],
        ],
        resize_keyboard=True,
    )


def subscribe_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📢 Kanalga obuna bo'lish", url=CHANNEL_URL)],
            [InlineKeyboardButton(text="✅ Tekshirish", callback_data="check")],
        ]
    )


def admin_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=BTN_STATS), KeyboardButton(text=BTN_BROADCAST)],
            [KeyboardButton(text=BTN_EXIT)],
        ],
        resize_keyboard=True,
    )


def cancel_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=BTN_CANCEL)]], resize_keyboard=True
    )
