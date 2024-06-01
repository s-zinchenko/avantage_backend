from django.db import models

from utils.files import upload_path


class Partner(models.Model):
    class Meta:
        verbose_name = "Партнёр"
        verbose_name_plural = "Партнёры"

    name = models.CharField(max_length=256, verbose_name="Имя партнёра")
    logo = models.FileField(
        verbose_name="Логотип партнёра",
        upload_to=upload_path,
    )

    def __str__(self) -> str:
        return self.name


class Rating(models.Model):
    class Meta:
        verbose_name = "Упоминание в рейтинге"
        verbose_name_plural = "Упоминания в рейтингах"

    name = models.CharField(max_length=256, verbose_name="Название рейтинга")
    logo = models.FileField(
        verbose_name="Логотип рейтинга",
        upload_to=upload_path,
    )
    link = models.CharField(max_length=1024, verbose_name="Ссылка на рейтинг", null=True)

    def __str__(self) -> str:
        return self.name
