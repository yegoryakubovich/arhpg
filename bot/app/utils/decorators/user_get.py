from datetime import datetime

from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from app.repositories import User, Text
from app.utils.api_client import api_client
from settings import settings

from app.repositories.oauth import Oauth

not_returned = False


def user_get(function):
    async def wrapper(*args):
        obj = args[0]
        tg_user_id = obj.from_user.id

        is_authorized = await User.is_authorized(tg_user_id=tg_user_id)
        if not is_authorized:
            oauth = await Oauth.create(tg_user_id=tg_user_id)
            redirect_url = settings.URL_OAUTH.format(hash=oauth.hash)

            kb = InlineKeyboardMarkup(row_width=1)
            kb.add(InlineKeyboardButton(
                text=Text.get('greetings_sso_button'),
                url=redirect_url,
            ))
            await obj.answer(text=Text.get('greetings'))
            await obj.answer(text=Text.get('greetings_sso'), reply_markup=kb)
            return

        user = await User.get(tg_user_id=tg_user_id)

        kwargs = {}

        if type(obj) is Message:
            kwargs['message'] = obj
        elif type(obj) is CallbackQuery:
            kwargs['callback_query'] = obj

        if not not_returned:
            kwargs['user'] = user

        return await function(**kwargs)

    return wrapper
