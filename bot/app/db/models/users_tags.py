from peewee import PrimaryKeyField, ForeignKeyField

from app.db.models.tag import Tag
from app.db.models.base import BaseModel
from app.db.models.user import User


class UserTag(BaseModel):
    id = PrimaryKeyField()
    user = ForeignKeyField(model=User, backref='users_tags', on_delete='cascade')
    tag = ForeignKeyField(model=Tag, backref='users_tags', on_delete='cascade')

    class Meta:
        db_table = 'users_tags'
