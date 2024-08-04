import asyncio
import os
import requests
from aiogram import Bot, Dispatcher, F

from aiogram.types import Message
from dotenv import load_dotenv


TG_API = os.getenv("TELEGRAM_TOKEN")
SERVER_URL = os.getenv("SERVER_URL")

bot = Bot(token=TG_API)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!"
                         f" Данный бот может запоминать твои сообщения, если ты этого захочешь. Введи 'Создать "
                         f"сообщение: ' и своё сообщение, бот запомнит его."
                         f"\nА командой /all_messages выведет все сообщения и их отправителей.")


@dp.message(F.text.startswith("Создать сообщение: "))
async def create_message_bot(message: Message):
    message_text = message.text.replace("Создать сообщение: ", "")
    user_data = {
        "is_bot": message.from_user.is_bot,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name or "",
        "username": message.from_user.username or "",
    }
    try:
        response = requests.post(''.join([SERVER_URL, "/api/v1/message/"]),
                                 json={"text": message_text,
                                       "from_f": user_data})
        response.raise_for_status()
        await message.answer("Сообщение успешно создано!")
    except requests.exceptions.RequestException as e:
        error_message = e.response.text if hasattr(e.response, 'text') else str(e)
        print(error_message)
        await message.answer(f"Ошибка при создании сообщения!")


@dp.message(F.text == "/all_messages")
async def all_messages(message: Message):
    try:
        response = requests.get(''.join([SERVER_URL, "/api/v1/messages/"]))
        response.raise_for_status()
        messages = response.json()

        all_messages_str = 'Сообщения: \n'

        for i in messages:
            msg_text = i.get("text")
            msg_from_name = i.get("from_f")['username']
            print(msg_text+msg_from_name)
            all_messages_str += msg_text + "\nОтправитель: @" + msg_from_name + "\n"
        await message.answer(all_messages_str)

    except requests.exceptions.RequestException as e:
        error_message = e.response.text if hasattr(e.response, 'text') else str(e)
        await message.answer(f"Ошибка при создании сообщения!")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
