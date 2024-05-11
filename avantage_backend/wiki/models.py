from django.db import models


class Letter(models.Model):
    class Meta:
        verbose_name = "Буква"
        verbose_name_plural = "Буквы"

    class Lang(models.TextChoices):
        RU = "ru"
        EN = "en"

    value = models.CharField(max_length=10, verbose_name="Буква")
    lang = models.CharField(max_length=32, null=True, choices=Lang.choices, verbose_name="Язык")
    site_lang = models.CharField(max_length=32, null=True, choices=Lang.choices, verbose_name="Язык сайта", default=Lang.RU)

    def __str__(self):
        return f"{self.value}, язык {self.lang}"


class Record(models.Model):
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    letter = models.ForeignKey(
        "wiki.Letter", on_delete=models.CASCADE, verbose_name="Буква"
    )
    title = models.CharField(max_length=512)
    external_link = models.CharField(max_length=512)

    def __str__(self):
        return self.title
