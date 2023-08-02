import warnings
from datetime import datetime, timezone
from warnings import filterwarnings

from loguru import logger

from app.aiogram import bot_get
from app.aiogram.kbs import Kbs
from app.db.manager import db_manager
from app.repositories import Oauth, User, Text
from app.utils.api_client import api_client


@db_manager
async def notificator_user():
    logger.info("notificator_user")
    bot = bot_get()
    for oauth in Oauth.list_get():
        if oauth.expired.replace(tzinfo=timezone.utc) <= datetime.now(timezone.utc):
            oauth.delete_instance()
        elif oauth.token:
            sso_user = await api_client.sso.user_get(token=oauth.token)
            arhpg_id = sso_user.get('unti_id')
            firstname = sso_user.get('firstname')
            lastname = sso_user.get('lastname')
            email = sso_user.get('email')

            if arhpg_id:
                await User.create(
                    arhpg_id=arhpg_id,
                    arhpg_token=oauth.token,
                    tg_user_id=oauth.tg_user_id,
                    firstname=firstname,
                    lastname=lastname,
                    email=email,
                )
                await api_client.user.add_tag_user(arhpg_id)
                # await States.menu.set()
                await bot.send_message(chat_id=oauth.tg_user_id, text=Text.get('menu'), reply_markup=await Kbs.menu())
                oauth.delete_instance()

    await bot.close()
