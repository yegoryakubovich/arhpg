from app.repositories.base import BaseRepository
from app.db.models import UserTagModel, UserModel, TagModel

class UserTag(BaseRepository):

    @staticmethod
    async def create(
            tag_id: TagModel,
            user_id: UserModel,
    ) -> UserTagModel:
        user_tag = UserTagModel(
            tag=tag_id,
            user=user_id,
        )
        user_tag.save()
        return user_tag