import asyncio
from aiogram import Bot, Dispatcher, F

from aiogram.types import Message

bot = Bot(token="12345678:AaBbCcDdEeFfGgHh")
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)
