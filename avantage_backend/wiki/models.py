from django.db import models


class Letter(models.Model):
    class Meta:
        verbose_name = "Буква"
        verbose_name_plural = "Буквы"

    value = models.CharField(max_length=1, unique=True, verbose_name="Буква")

    def __str__(self):
        return self.value


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
