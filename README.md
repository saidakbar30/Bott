# Carburator Bot (Qumtepa Karburator)

Telegram bot: karburator haqida, ustaxona manzili (lokatsiya + yozuv), narxlar, ish vaqti.
Majburiy obuna kanali: @karburatornew

## Tuzilma
- `bot.py` — ishga tushirish
- `config.py` — token, admin ID, kanal, koordinata, barcha matnlar
- `database.py` — SQLite (foydalanuvchilar)
- `keyboards.py` — tugmalar
- `middlewares.py` — majburiy obuna tekshiruvi
- `states.py` — admin xabar yuborish holati
- `utils.py` — yordamchi funksiyalar
- `handlers/user.py`, `handlers/admin.py`

## Ishga tushirish
1. `pip install -r requirements.txt`
2. `config.py` da `ADMIN_IDS`, `LAT`, `LON` ni to'ldiring
3. `BOT_TOKEN` ni muhit o'zgaruvchisiga (Replit Secrets) qo'ying
4. Botni @karburatornew kanaliga **admin** qiling
5. `python bot.py`

## Admin
`/admin` — statistika va hammaga xabar yuborish.

## Narx/matnni o'zgartirish
Faqat `config.py` dagi matnlarni tahrirlang.
