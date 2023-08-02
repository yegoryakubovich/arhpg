from django.db import models

from admin_web.models import Faq


class FaqAttachmentType:
    url = "url"
    file = "file"
    text = "text"
    image = "image"


class FaqAttachment(models.Model):
    class Meta:
        managed = False
        db_table = 'faqs_attachments'
        verbose_name = 'FAQ - Вложение'
        verbose_name_plural = 'FAQ - Вложения'

    id = models.AutoField(primary_key=True)

    faq = models.ForeignKey(Faq, on_delete=models.CASCADE, related_name="faqs_attachments_faq", verbose_name="FAQ")
    type = models.CharField(max_length=8, verbose_name="Тип")
    value = models.TextField(verbose_name="Значение")

    def __str__(self):
        return f"{self.faq} ({self.type})"
