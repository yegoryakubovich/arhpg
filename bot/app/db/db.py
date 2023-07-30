from peewee import MySQLDatabase

from settings import settings


db = MySQLDatabase(
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    database=settings.DB_NAME,
    charset='utf8mb4',
    autoconnect=False,
)

