import asyncio
from aiogram import Bot, Dispatcher

import os
from dotenv import load_dotenv

from app import handlers, states
from app.database.models import async_main


async def main():
    await async_main()
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(handlers.router, states.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
