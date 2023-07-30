from django.db import models


class Tag(models.Model):
    class Meta:
        managed = False
        db_table = 'tags'
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    id = models.AutoField(primary_key=True)

    tag_id = models.CharField(max_length=128, verbose_name="ID Тэга")
    name = models.CharField(max_length=128, verbose_name="Название")
    title = models.CharField(max_length=128, verbose_name="Заголовок")

    def __str__(self):
        return f"{self.name}"
