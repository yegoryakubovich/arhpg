from datetime import datetime, timezone

from app.db.manager import db_manager
from app.repositories import Oauth


@db_manager
async def notificator_user():
    current_datetime = datetime.now(timezone.utc)
    Oauth.delete_expired_tokens(current_datetime)
