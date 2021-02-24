# Модулі
import logging

from aiogram import Bot, Dispatcher
import asyncio

# Файли
import config
import update
import checker

TELEGRAM_API_KEY = config.TELEGRAM_API_KEY

# Логування
logging.basicConfig(level=logging.DEBUG)

# Ініціалізація
bot = Bot(token=TELEGRAM_API_KEY)
dp = Dispatcher(bot)

# Запуск
if __name__ == '__main__':
    update.Update().update()
    checker.delete_old_chatlog()
    asyncio.get_event_loop().run_until_complete(checker.checker())
