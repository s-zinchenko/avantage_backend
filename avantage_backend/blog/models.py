from django.db import models
from tinymce.models import HTMLField

from avantage_backend.share.enums import StrEnum
from utils.files import upload_path


class Article(models.Model):
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    title_ru = models.CharField(
        max_length=512, verbose_name="Название статьи (Ru)"
    )
    title_en = models.CharField(
        max_length=512, verbose_name="Название статьи (En)"
    )
    external_link = models.URLField(max_length=512, verbose_name="Ссылка")
    photo = models.FileField(
        verbose_name="Фото",
        upload_to=upload_path,
    )

    def __str__(self):
        return self.title_ru

    @property
    def ru(self):
        return {
            "id": self.id,
            "title": self.title_ru,
            "external_link": self.external_link,
            "photo": self.photo.url,
        }

    @property
    def en(self):
        return {
            "id": self.id,
            "title": self.title_en,
            "external_link": self.external_link,
            "photo": self.photo.url,
        }


class Customer(models.Model):
    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"

    name_ru = models.CharField(
        max_length=512, verbose_name="Название заказчика (Ru)"
    )
    name_en = models.CharField(
        max_length=512, verbose_name="Название заказчика (En)"
    )
    type_ru = models.CharField(
        max_length=512, verbose_name="Тип заказчика (Ru)"
    )
    type_en = models.CharField(
        max_length=512, verbose_name="Тип заказчика (En)"
    )

    def __str__(self):
        return self.name_ru

    @property
    def ru(self):
        return {
            "id": self.id,
            "name": self.name_ru,
            "type": self.type_ru,
        }

    @property
    def en(self):
        return {
            "id": self.id,
            "name": self.name_en,
            "type": self.type_en,
        }


class CaseAttachment(models.Model):
    class Meta:
        verbose_name = "Вложение кейса"
        verbose_name_plural = "Вложения кейсов"

    class ContentType(models.TextChoices):
        IMAGE = "image"
        VIDEO = "video"

    file = models.FileField(
        verbose_name="Файл",
        upload_to=upload_path,
    )
    case = models.ForeignKey(
        "blog.Case", on_delete=models.CASCADE, verbose_name="Кейс"
    )
    is_main = models.BooleanField(verbose_name="Основное", default=False)
    content_type = models.CharField(
        max_length=512,
        choices=ContentType.choices,
        verbose_name="Тип содержимого",
        default=ContentType.IMAGE,
    )

    def __str__(self):
        return f"Вложение для кейса {self.case_id}"


class Case(models.Model):
    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"

    class TypeRU(StrEnum):
        INTERNAL = "ВНУТРЕННИЕ КОММУНИКАЦИИ"
        EXTERNAL = "ВНЕШНИЕ КОММУНИКАЦИИ"

    class TypeEN(StrEnum):
        INTERNAL = "INTERNAL COMMUNICATIONS"
        EXTERNAL = "EXTERNAL COMMUNICATIONS"

    title_ru = models.CharField(
        max_length=512, verbose_name="Название кейса (Ru)"
    )
    title_en = models.CharField(
        max_length=512, verbose_name="Название кейса (En)"
    )
    year = models.CharField(verbose_name="Год проведения", null=True, max_length=32)
    customer = models.ForeignKey(
        "blog.Customer", on_delete=models.CASCADE, verbose_name="Заказчик"
    )
    body_ru = HTMLField(verbose_name="Описание (Ru)", null=True, blank=True)
    body_en = HTMLField(verbose_name="Описание (En)", null=True, blank=True)
    type_ru = models.CharField(
        max_length=512,
        choices=((key, key) for key in list(TypeRU)),
        verbose_name="Тип кейса (Ru)",
    )
    type_en = models.CharField(
        max_length=512,
        choices=((key, key) for key in list(TypeEN)),
        verbose_name="Тип кейса (En)",
    )
    show_on_main_page = models.BooleanField(
        verbose_name="Показывать на главной странице", default=False
    )
    cover_image = models.FileField(
        verbose_name="Обложка",
        upload_to=upload_path,
        null=True
    )

    def __str__(self):
        return self.title_ru

    @property
    def ru(self):
        return {
            "id": self.id,
            "title": self.title_ru,
            "year": self.year,
            "customer": self.customer,
            "body": self.body_ru,
            "type": self.type_ru,
            "show_on_main_page": self.show_on_main_page,
            "cover_image": self.cover_image.url if self.cover_image else None,
        }

    @property
    def en(self):
        return {
            "id": self.id,
            "title": self.title_en,
            "year": self.year,
            "customer": self.customer,
            "body": self.body_en,
            "type": self.type_en,
            "show_on_main_page": self.show_on_main_page,
            "cover_image": self.cover_image.url if self.cover_image else None,
        }
