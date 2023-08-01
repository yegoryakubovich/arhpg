from app.repositories.base import BaseRepository
from app.db.models import UserTagModel, UserModel, TagModel

class UserTag(BaseRepository):

    @staticmethod
    async def create(
            tag: TagModel,
            user: UserModel,
    ) -> UserTagModel:
        user_tag = UserTagModel(
            tag=tag,
            user=user,
        )
        user_tag.save()
        return user_tag

    @staticmethod
    async def get_user_tag(user_id, tag_id):
        tag_user = UserTagModel.get_or_none((UserTagModel.user == user_id) & (UserTagModel.tag == tag_id))
        return tag_user
