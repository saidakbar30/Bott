from aiogram import Bot, F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

import config
from keyboards import BTN_ABOUT, BTN_ADDR, BTN_PRICE, BTN_TIME, main_menu
from utils import is_subscribed

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(config.WELCOME, reply_markup=main_menu())


@router.callback_query(F.data == "check")
async def check_sub(call: CallbackQuery, bot: Bot):
    if await is_subscribed(bot, call.from_user.id):
        await call.message.delete()
        await call.message.answer(config.WELCOME, reply_markup=main_menu())
    else:
        await call.answer("Siz hali obuna bo'lmadingiz!", show_alert=True)


@router.message(F.text == BTN_ABOUT)
async def about(message: Message):
    await message.answer(config.ABOUT)


@router.message(F.text == BTN_PRICE)
async def prices(message: Message):
    await message.answer(config.PRICES)


@router.message(F.text == BTN_TIME)
async def work_time(message: Message):
    await message.answer(config.WORK_TIME)


@router.message(F.text == BTN_ADDR)
async def address(message: Message):
    await message.answer_location(config.LAT, config.LON)
    await message.answer(config.ADDRESS)
