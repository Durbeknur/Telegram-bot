import asyncio
import nest_asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

nest_asyncio.apply()

# Boshlanish
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Beeline", callback_data='beeline')],
        [InlineKeyboardButton("Ucell", callback_data='ucell')],
        [InlineKeyboardButton("Uzmobile", callback_data='uzmobile')],
        [InlineKeyboardButton("Mobiuz", callback_data='mobiuz')],
        [InlineKeyboardButton("OQ", callback_data='oq')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Qaysi kompaniya kerak?", reply_markup=reply_markup)

# Callback tugmalar
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "beeline":
        keyboard = [
            [InlineKeyboardButton("Tariflar", callback_data='beeline_tarif')],
            [InlineKeyboardButton("Xizmatlar", callback_data='xizmat')],
            [InlineKeyboardButton("Yangiliklar", callback_data='yangilik')],
        ]
        await query.edit_message_text("Beeline menyusi:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "beeline_tarif":
        keyboard = [
            [InlineKeyboardButton("MULTI Kuch", callback_data='multi_kuch')],
            [InlineKeyboardButton("Status", callback_data='status')],
            [InlineKeyboardButton("Konstruktor", callback_data='konstruktor')],
            [InlineKeyboardButton("Oila", callback_data='oila')],
            [InlineKeyboardButton("Boshqa", callback_data='boshqa')],
        ]
        await query.edit_message_text("Beeline tariflari:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "multi_kuch":
        keyboard = [
            [InlineKeyboardButton("MULTI Plus", callback_data='multi_plus')],
            [InlineKeyboardButton("MULTI Pro", callback_data='multi_pro')],
            [InlineKeyboardButton("MULTI Max", callback_data='multi_max')],
        ]
        await query.edit_message_text("MULTI Kuch bo'limi:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "multi_plus":
        text = """📦 MULTI Plus tarifi:
49 900 so'm/oy
📞 Cheksiz qo'ng'iroqlar
📨 500 SMS
🌐 25 GB + tungi cheksiz internet
🎬 Kinom obunasi
💸 Beepulda 5 mln so'mgacha o'tkazma
💪 +1 kuch tanlovga"""
        await query.edit_message_text(text)

    elif query.data == "multi_pro":
        text = """📦 MULTI Pro tarifi:
69 900 so'm/oy
📞 Cheksiz qo'ng'iroqlar
📨 500 SMS
🌐 50 GB + tungi cheksiz internet
🎬 Kinom obunasi
💸 Beepulda 10 mln so'mgacha o'tkazma
💪 +2 kuch tanlovga"""
        await query.edit_message_text(text)

    elif query.data == "multi_max":
        text = """📦 MULTI Max tarifi:
89 900 so'm/oy
📞 Cheksiz qo'ng'iroqlar
📨 500 SMS
🌐 80 GB + tungi cheksiz internet
🎬 Kinom obunasi
💸 Beepulda 15 mln so'mgacha o'tkazma
💪 +3 kuch tanlovga"""
        await query.edit_message_text(text)

    elif query.data == "oila":
        keyboard = [
            [InlineKeyboardButton("Oila Start", callback_data='oila_start')],
            [InlineKeyboardButton("Oila Max", callback_data='oila_max')],
            [InlineKeyboardButton("Oila Ultra", callback_data='oila_ultra')],
        ]
        await query.edit_message_text("Oila tariflari:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "oila_start":
        text = """👨‍👩‍👧‍👦 OILA Start:
🆕 Yangi ulanishlar uchun
💰 48 000 so'm/oy (3 oy), keyin 60 000 so'm/oy
👥 Guruhda 2 raqam
🌐 50 GB + tungi cheksiz internet
📞 Cheksiz qo‘ng‘iroqlar
📨 1000 SMS
🎬 Setanta Sports + Kinom
💸 Beepulda 10 mln so’mgacha 0% o'tkazma"""
        await query.edit_message_text(text)

    elif query.data == "oila_max":
        text = """👨‍👩‍👧‍👦 OILA Max:
💰 100 000 so'm/oy
🎁 Yangi ulanishda 3 oyga 20% chegirma
👥 Guruhda 3 raqam
🌐 120 GB + tungi cheksiz internet
📞 Cheksiz qo‘ng‘iroqlar
📨 1000 SMS
🎬 Setanta Sports + Kinom
💸 Beepulda 30 mln so’mgacha 0% o'tkazma"""
        await query.edit_message_text(text)

    elif query.data == "oila_ultra":
        text = """👨‍👩‍👧‍👦 OILA Ultra:
💰 150 000 so'm/oy
🎁 Yangi ulanishda 3 oyga 20% chegirma
👥 Guruhda 5 raqam
🌐 250 GB + tungi cheksiz internet
📞 Cheksiz qo‘ng‘iroqlar
📨 1000 SMS
🎬 Setanta Sports + Kinom
💸 Beepulda 50 mln so’mgacha 0% o'tkazma"""


    else:
        await query.edit_message_text(f"Bo'lim: {query.data}")

# Asosiy funksiya
async def main():
    app = ApplicationBuilder().token("7820609583:AAFWZ4dT2rzq_O_5Q70USeklL-N3ij-oX4s").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot ishga tushdi!")
    await app.run_polling()

# Bosh loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
