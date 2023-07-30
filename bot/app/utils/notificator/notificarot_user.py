from datetime import datetime, timezone

from app.db.manager import db_manager
from app.repositories import Oauth


@db_manager
async def notificator_user():
    current_datetime = datetime.now(timezone.utc)
    Oauth.delete_expired_tokens(current_datetime)
    for oauth in Oauth.list_get():
        if oauth.expired >= datetime.now(timezone.utc):
            oauth.delete_instance()
        elif oauth.token:
            pass
            # -> добавление юзера, уведомление ему, перекидывание в меню
