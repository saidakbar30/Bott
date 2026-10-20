
import asyncio

from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import database as db
from config import ADMIN_IDS
from keyboards import (
    BTN_BROADCAST,
    BTN_CANCEL,
    BTN_EXIT,
    BTN_STATS,
    admin_menu,
    cancel_kb,
    main_menu,
)
from states import Broadcast

router = Router()
router.message.filter(F.from_user.id.in_(ADMIN_IDS))


@router.message(Command("admin"))
async def admin_panel(message: Message):
    await message.answer("👨‍💻 Admin panel", reply_markup=admin_menu())


@router.message(F.text == BTN_EXIT)
async def exit_admin(message: Message):
    await message.answer("Asosiy menyu", reply_markup=main_menu())


@router.message(F.text == BTN_STATS)
async def stats(message: Message):
    await message.answer(
        f"📊 <b>Statistika</b>\n\n"
        f"👥 Jami foydalanuvchilar: <b>{db.count_users()}</b>\n"
        f"🆕 Bugun qo'shilganlar: <b>{db.count_today()}</b>"
    )


@router.message(F.text == BTN_BROADCAST)
async def broadcast_start(message: Message, state: FSMContext):
    await state.set_state(Broadcast.waiting_message)
    await message.answer(
        "Hammaga yuboriladigan xabarni yuboring (matn, rasm, video...):",
        reply_markup=cancel_kb(),
    )


@router.message(Broadcast.waiting_message, F.text == BTN_CANCEL)
async def broadcast_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Bekor qilindi.", reply_markup=admin_menu())


@router.message(Broadcast.waiting_message)
async def broadcast_send(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    ok = fail = 0
    for uid in db.all_user_ids():
        try:
            await bot.copy_message(uid, message.chat.id, message.message_id)
            ok += 1
        except Exception:
            fail += 1
        await asyncio.sleep(0.05)
    await message.answer(
        f"✅ Yuborildi: {ok}\n❌ Yetib bormadi: {fail}", reply_markup=admin_menu()
  )
  
