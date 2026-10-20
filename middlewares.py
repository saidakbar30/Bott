from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery

import database as db
from config import ADMIN_IDS
from keyboards import subscribe_kb
from utils import is_subscribed

SUB_TEXT = "❗ Botdan foydalanish uchun avval kanalimizga obuna bo'ling:"


class SubscriptionMiddleware(BaseMiddleware):
    """Har bir xabar/tugmada: foydalanuvchini bazaga yozadi va
    kanalga obunani tekshiradi."""

    async def __call__(self, handler, event, data):
        user = data.get("event_from_user")
        if user is None:
            return await handler(event, data)

        db.add_user(user.id, user.full_name, user.username)

        # adminlar va "Tekshirish" tugmasi o'tkazib yuboriladi
        if user.id in ADMIN_IDS:
            return await handler(event, data)
        if isinstance(event, CallbackQuery) and event.data == "check":
            return await handler(event, data)

        if await is_subscribed(data["bot"], user.id):
            return await handler(event, data)

        if isinstance(event, CallbackQuery):
            await event.answer("Avval kanalga obuna bo'ling!", show_alert=True)
        else:
            await event.answer(SUB_TEXT, reply_markup=subscribe_kb())
