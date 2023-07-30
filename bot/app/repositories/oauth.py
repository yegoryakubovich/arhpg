from datetime import datetime, timezone, timedelta

from app.repositories.base import BaseRepository
from app.db.models import OauthModel
from hashlib import md5


class Oauth(BaseRepository):
    @staticmethod
    async def create(tg_user_id: int, token: str, expired: datetime) -> OauthModel:
        user = OauthModel.get_or_none(OauthModel.tg_user_id == tg_user_id)
        if not user:
            random_hash = md5(str(tg_user_id).encode()).hexdigest()
            if expired:
                utc_timezone = timezone.utc
                expired = expired + timedelta(minutes=30)
                expired = expired.astimezone(utc_timezone)
            user = OauthModel(
                tg_user_id=tg_user_id,
                hash=random_hash,
                token=token,
                expired=expired
            )
            user.save()
        return user

    @staticmethod
    def list_token_get():
        tokens = OauthModel.select().where(OauthModel.token.is_null(False))
        return tokens

    @staticmethod
    def delete_expired_tokens(current_datetime: datetime):
        utc_current_datetime = current_datetime.astimezone(timezone.utc)
        expired_tokens = OauthModel.select().where(OauthModel.expired <= utc_current_datetime)
        for token in expired_tokens:
            token.delete_instance()