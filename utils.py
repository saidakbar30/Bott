from aiogram import Bot

from config import CHANNEL


async def is_subscribed(bot: Bot, user_id: int) -> bool:
    """Foydalanuvchi kanalga obuna bo'lganini tekshiradi.
    Bot kanalda admin bo'lishi shart."""
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in ("member", "administrator", "creator")
    except Exception:
        return False
