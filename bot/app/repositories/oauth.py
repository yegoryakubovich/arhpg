from datetime import datetime, timezone, timedelta

from app.repositories.base import BaseRepository
from app.db.models import OauthModel
from hashlib import md5


class Oauth(BaseRepository):
    @staticmethod
    async def create(tg_user_id: int) -> OauthModel:
        user = OauthModel.get_or_none(OauthModel.tg_user_id == tg_user_id)
        if not user:
            random_hash = md5(str(tg_user_id).encode()).hexdigest()
            expired = datetime.now(timezone.utc) + timedelta(minutes=30)

            user = OauthModel(
                tg_user_id=tg_user_id,
                hash=random_hash,
                expired=expired
            )
            user.save()
        return user

    @staticmethod
    def list_get() -> list[OauthModel]:
        oauths = OauthModel.select().execute()
        return oauths
