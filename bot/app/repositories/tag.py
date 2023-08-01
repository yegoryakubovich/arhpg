from app.repositories.base import BaseRepository
from app.db.models import TagModel

class Tag(BaseRepository):

    @staticmethod
    async def create(
            tag_id: int,
            name: str,
            title: str,
    ) -> TagModel:
        tag = TagModel(
            tag_id=tag_id,
            name=name,
            title=title,
        )
        tag.save()
        return tag

    @staticmethod
    async def get():
        tag = TagModel.select().execute()
        return tag

    @staticmethod
    async def list_tag_get():
        tag = TagModel.select().where(TagModel.tag_id == TagModel.tag_id).execute()
        return tag


