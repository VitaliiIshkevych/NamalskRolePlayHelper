# Модулі
import lxml.html
import requests
import os
import zipfile
import shutil

# Файли
import config


# Код
class Update:
    def __init__(self):
        self.version = float(lxml.html.document_fromstring(requests.get(config.GITHUB_REPOSITORY_URL).text).xpath(
            "//*[@id=\"readme\"]/div[3]/article/h1[2]/text()")[0].split(" ")[-1])

    def update(self):
        if self.version == config.VERSION:
            pass
        else:
            # Скачати оновлення
            file = open(f"C:\\Users\\{os.getlogin()}\\Desktop\\NamalskRolePlayHelper.zip", "wb")
            content = requests.get(f"{config.GITHUB_REPOSITORY_DOWNLOAD_URL}")
            file.write(content.content)
            file.close()
            # Розархівувати оновлення
            archive = zipfile.ZipFile(f"C:\\Users\\{os.getlogin()}\\Desktop\\NamalskRolePlayHelper.zip")
            archive.extractall(f"C:\\Users\\{os.getlogin()}\\Desktop")
            archive.close()
            # Перейменувати оновлення
            os.rename(f"C:\\Users\\{os.getlogin()}\\Desktop\\NamalskRolePlayHelper-main",
                      f"C:\\Users\\{os.getlogin()}\\Desktop\\NamalskRolePlayHelper-v{self.version}")
            # Видалити стару версію
            try:
                shutil.rmtree(f"C:\\Users\\{os.getlogin()}\\Desktop\\NamalskRolePlayHelper\\NamalskRolePlayHelper")
            except IOError:
                pass
            # Встановити нову версію
            shutil.move(
                f"C:\\Users\\{os.getlogin()}\\Desktop\\NamalskRolePlayHelper-v{self.version}\\NamalskRolePlayHelper",
                f"C:\\Users\\{os.getlogin()}\\Desktop\\NamalskRolePlayHelper\\NamalskRolePlayHelper")
            # Видалити тимчасові файли
            os.remove(f"C:\\Users\\{os.getlogin()}\\Desktop\\NamalskRolePlayHelper.zip")
            shutil.rmtree(f"C:\\Users\\{os.getlogin()}\\Desktop\\NamalskRolePlayHelper-v{self.version}")
