from peewee import PrimaryKeyField, BigIntegerField, CharField, DateTimeField

from app.db.models.base import BaseModel


class Oauth(BaseModel):
    id = PrimaryKeyField()
    tg_user_id = BigIntegerField()
    hash = CharField(max_length=1024)
    token = CharField(max_length=1024, null=True, default=None)
    expired = DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'oauths'