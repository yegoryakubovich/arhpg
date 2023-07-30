
from aiogram import Bot

from settings import settings


def bot_get():
    bot = Bot(
        token=settings.TG_BOT_TOKEN,
    )
    return bot

