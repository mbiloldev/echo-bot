import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# ✅ Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# 🔑 Token
BOT_TOKEN = "YOUR_TOKEN_HERE"

# 🤖 Bot va Dispatcher — 3.7.0+ usuli
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


# /start komandasi
@dp.message(CommandStart())
async def start_handler(message: Message):
    user = message.from_user
    await message.answer(
        f"👋 Assalomu alaykum, <b>{user.full_name}</b>!\n\n"
        f"🤖 Men <b>Echo Bot</b>man — siz yozgan har qanday xabarni sizga qaytarib beraman.\n\n"
        f"💬 Menga istalgan narsa yozing, men takrorlayman! 🎉"
    )


# Har qanday matn xabarni echo qilish
@dp.message(F.text)
async def echo_handler(message: Message):
    await message.copy_to(message.chat.id)


# Boshqa turdagi xabarlar (rasm, video, sticker va h.k.)
@dp.message()
async def unknown_handler(message: Message):
    await message.answer("⚠️ Men faqat matn xabarlarni qaytara olaman!")


# 🚀 Botni ishga tushirish
async def main():
    logger.info("Bot ishga tushmoqda...")
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
