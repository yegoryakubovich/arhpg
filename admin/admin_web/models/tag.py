from django.db import models


class Tag(models.Model):
    class Meta:
        managed = False
        db_table = 'tags'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    id = models.AutoField(primary_key=True)

    tag_id = models.CharField(max_length=128, verbose_name="ID Тега")
    name = models.CharField(max_length=128, verbose_name="Название")
    title = models.CharField(max_length=128, verbose_name="Заголовок")

    def __str__(self):
        return f"{self.name}"
