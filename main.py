import asyncio
import logging

from aiogram import Dispatcher, Bot, F, types
from aiogram.methods import DeleteWebhook
from bot_token import TOKEN

dp = Dispatcher()
mybot = Bot(token=TOKEN)


@dp.business_message()
async def back_to_work(message: types.Message):
    await message.answer(text=f'Это спам-сообщение в ответ на твое сообщение')


async def main():
    logging.basicConfig(level=logging.INFO)
    await mybot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(mybot)


if __name__ == "__main__":
    asyncio.run(main())

