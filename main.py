import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from config import BOT_TOKEN
from src.handlers import router


bot = Bot(token=BOT_TOKEN)      # это обьект или экземпляр класса
dp = Dispatcher()               # обработчик входящих обновлений


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

