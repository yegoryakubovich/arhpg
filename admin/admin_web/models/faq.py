from django.db import models


class FaqType:
    text = "text"
    link = "link"


class Faq(models.Model):
    class Meta:
        managed = False
        db_table = 'faqs'
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    id = models.AutoField(primary_key=True)

    priority = models.IntegerField(verbose_name="Приоритет")
    type = models.CharField(max_length=8, verbose_name="Тип",
                            choices=((FaqType.text, "Текст"), (FaqType.link, "Ссылка")))  # url, text
    question = models.CharField(max_length=2048, verbose_name="Вопрос")
    answer_button = models.CharField(max_length=2048, verbose_name="Кнопка ответа")

    def __str__(self):
        return f"{self.question}"
