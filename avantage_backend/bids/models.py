from typing import Dict

from django.db import models

from avantage_backend.bids.mixins import SendEmailMixin


class CooperationBid(SendEmailMixin, models.Model):
    class Meta:
        verbose_name = "Заявка на сотрудничество"
        verbose_name_plural = "Заявки на сотрудничество"

    email_subject: str = "Заявка на сотрудничество"
    email_recipient = "avantage@avantage-event.com"

    full_name = models.CharField(max_length=512, verbose_name="Полное имя")
    contact_phone = models.CharField(
        max_length=32, verbose_name="Контактный телефон"
    )
    email = models.EmailField(verbose_name="Электронная почта")
    project_scope = models.TextField(
        verbose_name="Сфера проекта", null=True, blank=True
    )
    project_goals = models.TextField(verbose_name="Цели и задачи проекта")

    def __str__(self) -> str:
        return f"{self.full_name} {self.contact_phone}"

    @property
    def to_dict(self) -> Dict[str, str]:
        return {
            "Полное имя:": self.full_name,
            "Контактный телефон:": self.contact_phone,
            "Электронная почта:": self.email,
            "Сфера проекта:": self.project_scope,
            "Цели и задачи проекта:": self.project_goals,
        }
