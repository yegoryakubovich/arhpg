from django.db import models

from admin_web.models import Tag


class User(models.Model):
    class Meta:
        managed = False
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    id = models.AutoField(primary_key=True)

    arhpg_id = models.BigIntegerField(verbose_name="Arhpg ID")
    arhpg_token = models.CharField(max_length=1024, verbose_name="Arhpg Token")
    tg_user_id = models.BigIntegerField(verbose_name="ID Telegram")
    firstname = models.CharField(max_length=128, null=True, blank=True, verbose_name="Имя")
    lastname = models.CharField(max_length=128, null=True, blank=True, verbose_name="Фамилия")
    email = models.CharField(max_length=256, null=True, blank=True, verbose_name="Почта")

    tags = models.ManyToManyField(Tag, related_name="users_tags", verbose_name="Тэги")

    def __str__(self):
        return f"{self.id} - {self.firstname}"
