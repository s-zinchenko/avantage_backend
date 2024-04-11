from django.db import models

from utils.files import upload_path


class Product(models.Model):
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    title_ru = models.CharField(
        max_length=512, verbose_name="Название услуги (Ru)"
    )
    title_en = models.CharField(
        max_length=512, verbose_name="Название услуги (En)"
    )
    description_ru = models.CharField(
        max_length=1024, verbose_name="Описание (Ru)"
    )
    description_en = models.CharField(
        max_length=1024, verbose_name="Описание (En)"
    )
    order = models.PositiveIntegerField(verbose_name="Порядковый номер")
    external_link = models.CharField(
        max_length=512, verbose_name="Ссылка", blank=True, null=True
    )
    background_image = models.FileField(
        verbose_name="Фото",
        upload_to=upload_path,
        null=True,
        blank=True
    )
    events_ru = models.TextField(verbose_name="События (Ru)")
    events_en = models.TextField(verbose_name="События (En)")

    def __str__(self) -> str:
        return self.title_ru

    @property
    def ru(self):
        return {
            "id": self.id,
            "title": self.title_ru,
            "description": self.description_ru,
            "order": self.order,
            "external_link": self.external_link,
            "events": self.events_ru,
            "background_image": self.background_image.url if self.background_image else None,
        }

    @property
    def en(self):
        return {
            "id": self.id,
            "title": self.title_en,
            "description": self.description_en,
            "order": self.order,
            "external_link": self.external_link,
            "events": self.events_en,
            "background_image": self.background_image.url if self.background_image else None,
        }
