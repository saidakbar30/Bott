import os

# ====== SOZLAMALAR ======
BOT_TOKEN = os.getenv("BOT_TOKEN", "BU_YERGA_TOKEN")
ADMIN_IDS = [0]  # o'zingizning Telegram ID'ingiz (bir nechta bo'lsa vergul bilan)

CHANNEL = "@karburatornew"
CHANNEL_URL = "https://t.me/karburatornew"

# Ustaxona lokatsiyasi (Google Maps'dan koordinata oling)
LAT = 40.45399
LON = 71.66339

DB_PATH = "carburator.db"

# ====== MATNLAR ======
WELCOME = (
    "👋 Assalomu alaykum!\n\n"
    "Qumtepa Karburator botiga xush kelibsiz.\n"
    "Kerakli bo'limni tanlang 👇"
)

ABOUT = (
    "🔧 <b>Changan (Xitoy) karburatorini o'rnatish</b>\n"
    "(Damas va Labo uchun eng samarali yechim)\n\n"
    "🔹 Xitoy karburatori narxi: <b>350 000 so'm</b>\n"
    "🔹 O'rnatib berish (ustanovka): <b>150 000 so'm</b>\n\n"
    "📊 <b>Real test va rasxod ko'rsatkichlari:</b>\n"
    "• To'g'ri o'rnatilgan Xitoy karburatori 100 km ga "
    "<b>5,5 – 6 litr</b> benzin sarflaydi!\n"
    "• Amaliy test natijamiz: <b>1 litr</b> benzin bilan "
    "<b>18 km</b> masofa bosib o'tildi!"
)

PRICES = (
    "🔹 Xitoy karburatori narxi: 350 000 so'm\n\n"
    "🔹 O'rnatib berish (Ustanovka): 150 000 so'm\n\n"
    "Original karburator tozalash (zapchastlari bilan): 200 000 so'm\n\n"
    "• Igna-klapan sozlash: 40 000 so'm\n\n"
    "• Svecha almashtirish (narxi kelishiladi)\n\n"
    "• Avto elektrik xizmatlari (ham bor)\n\n"
    "• Xolostoy yurishni sozlash (Instagramga obuna bo'lib kelganga tekin)\n\n"
    "• Umumiy texnik ko'rik (ham bor)"
)

WORK_TIME = "⏰ Ish vaqti: 08:00 – 19:00\n\n❌ Dam olish kuni: Payshanba"

ADDRESS = "📍 FARG'ONA, MARG'ILON SHAHRI, QUMTEPA KURUG OLDIDA"
