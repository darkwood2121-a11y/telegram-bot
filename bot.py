import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7303927724:AAGB4Mq2JaJQObpkl-PUBh0WxUL1Gws2tD8"
OWNER_ID = 7303984536  # ← ТВІЙ TELEGRAM ID

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📩 Зв’язатися з менеджером", callback_data="contact")]
        ]
    )
    await message.answer(
        "Вітаємо! 👋\nНатисніть кнопку нижче, щоб зв’язатися з менеджером.",
        reply_markup=kb
    )

@dp.callback_query(lambda c: c.data == "contact")
async def contact(callback: types.CallbackQuery):
    user = callback.from_user

    text = (
        "📥 НОВИЙ КЛІЄНТ\n\n"
        f"👤 Ім’я: {user.full_name}\n"
        f"🔗 Username: @{user.username if user.username else 'немає'}\n"
        f"🆔 ID: {user.id}"
    )

    await bot.send_message(OWNER_ID, text)
    await callback.message.answer(
        "✅ Заявку надіслано! Менеджер незабаром напише вам."
    )
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
