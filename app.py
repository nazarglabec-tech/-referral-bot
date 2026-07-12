from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

import os
import asyncio

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

async def main():
    print("✅ Bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())