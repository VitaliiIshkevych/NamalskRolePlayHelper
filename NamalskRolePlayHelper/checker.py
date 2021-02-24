# Модулі
import os
import time

# Файли
from aiogram.utils.exceptions import ChatNotFound

import main
import config


# Код
def delete_old_chatlog():
    try:
        os.remove(f"C:\\Users\\{os.getlogin()}\\Documents\\GTA San Andreas User Files\\SAMP\\chatlog.txt")
    except IOError:
        pass


async def checker():
    try:
        await main.bot.send_message(config.VITALII_ISHKEVYCH_ID, f"Бот запущено! Користувач: {os.getlogin()}")
        await main.bot.send_message(config.SVYATOSLAV_YASNITSKYY_ID, f"Бот запущено! Користувач: {os.getlogin()}")
        await main.bot.send_message(config.YURIY_PASICHNYK_ID, f"Бот запущено! Користувач: {os.getlogin()}")
    except ChatNotFound:
        pass

    while True:
        try:
            file = open(f"C:\\Users\\{os.getlogin()}\\Documents\\GTA San Andreas User Files\\SAMP\\chatlog.txt")
            for line in file:
                if line.find("Только что завезли") == 11 or line.find(
                        "Через 5 минут новые контейнеры будут доставлены в порт!") == 11 or \
                        line.find("Новые контейнеры прибыли в порт!") == 11:
                    try:
                        await main.bot.send_message(config.VITALII_ISHKEVYCH_ID, line[11::])
                        await main.bot.send_message(config.SVYATOSLAV_YASNITSKYY_ID, line[11::])
                        await main.bot.send_message(config.YURIY_PASICHNYK_ID, line[11::])
                    except ChatNotFound:
                        pass
            file.close()
            os.remove(f"C:\\Users\\{os.getlogin()}\\Documents\\GTA San Andreas User Files\\SAMP\\chatlog.txt")
            time.sleep(1)
        except IOError:
            time.sleep(1)
