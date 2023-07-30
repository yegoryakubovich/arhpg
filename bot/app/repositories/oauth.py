from app.repositories.base import BaseRepository
from app.db.models import OauthModel
from hashlib import md5

class Oauth(BaseRepository):
    @staticmethod
    async def create(tg_user_id: int, token: None, expired: None) -> OauthModel:
        user = OauthModel.get_or_none(OauthModel.tg_user_id == tg_user_id)
        if not user:
            random_hash = md5(str(tg_user_id).encode())
            user = OauthModel(
                tg_user_id=tg_user_id,
                hash=random_hash,
                token=token,
                expired=expired
            )
            user.save()
        return user