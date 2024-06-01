# type: ignore
from typing import Dict

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

from utils.files import upload_path


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self, email: str, password: str, **extra_fields: Dict
    ) -> AbstractBaseUser:
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, email: str = None, password: str = None, **extra_fields
    ) -> AbstractBaseUser:
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(
        self, email: str, password: str, **extra_fields
    ) -> AbstractBaseUser:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    email = models.EmailField("E-mail", unique=True)
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log " "into this admin site."
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    def get_short_name(self):
        return self.email


class Company(SingletonModel):
    class Meta:
        verbose_name = "Компания"

    # основная информация
    greeting_title_ru = models.CharField(
        max_length=255, verbose_name="Приветственный заголовок (RU)"
    )
    greeting_title_en = models.CharField(
        max_length=255, verbose_name="Приветственный заголовок (EN)"
    )
    greeting_description_ru = models.TextField(
        verbose_name="Приветственное описание (RU)"
    )
    greeting_description_en = models.TextField(
        verbose_name="Приветственное описание (EN)"
    )
    about_image = models.FileField(
        verbose_name="Изображение о компании",
        upload_to=upload_path,
    )
    about_text_ru = models.TextField(verbose_name="О компании (RU)")
    about_text_en = models.TextField(verbose_name="О компании (EN)")
    intro_video = models.FileField(
        verbose_name="Шоурил",
        upload_to=upload_path,
    )
    interview = models.FileField(
        verbose_name="Презентация о компании", upload_to=upload_path
    )
    welcome_video = models.FileField(
        verbose_name="Приветственное видео", upload_to=upload_path
    )
    years_of_experience = models.PositiveIntegerField(verbose_name="Годы опыта")
    unique_scenarios = models.PositiveIntegerField(
        verbose_name="Уникальных сценарии"
    )
    implemented_projects = models.PositiveIntegerField(
        verbose_name="Реализованных проектов"
    )
    # контакты
    address_ru = models.CharField(max_length=256, verbose_name="Адрес (RU)")
    address_en = models.CharField(max_length=256, verbose_name="Адрес (EN)")
    contact_phone = models.CharField(
        max_length=256, verbose_name="Контактный телефон"
    )
    contact_email = models.EmailField(verbose_name="Контактная почта")
    telegram = models.CharField(max_length=256, verbose_name="Телеграм")
    ok = models.CharField(max_length=256, verbose_name="Одноклассники", null=True)
    vk = models.CharField(max_length=256, verbose_name="ВКонтакте", null=True)
    email_for_clients = models.CharField(max_length=1024,verbose_name="Email для клиентов")
    email_for_mass_media = models.EmailField(
        verbose_name="Email для СМИ"
    )
    email_for_partners = models.EmailField(
        verbose_name="Email для партнёров", null=True
    )
    email_for_applicant = models.EmailField(
        verbose_name="Email для соискателей"
    )
    # файлы
    portfolio = models.FileField(
        verbose_name="Портфолио",
        upload_to=upload_path,
    )
    requisites = models.FileField(
        verbose_name="Реквизиты",
        upload_to=upload_path,
    )
    presentation = models.FileField(
        verbose_name="Презентация",
        upload_to=upload_path,
    )
    brief = models.FileField(
        verbose_name="Бриф",
        upload_to=upload_path,
    )
    agreement = models.FileField(
        verbose_name="Согласие на обработку персональных данных",
        upload_to=upload_path,
    )
    form_for_freelancers = models.FileField(
        verbose_name="Форма для фрилансеров",
        upload_to=upload_path,
    )

    def __str__(self) -> str:
        return "Компания"

    @property
    def ru(self):
        return {
            "greeting_title": self.greeting_title_ru,
            "greeting_description": self.greeting_description_ru,
            "about_image": self.about_image.url,
            "about_text": self.about_text_ru,
            "intro_video": self.intro_video.url,
            "interview": self.interview.url,
            "welcome_video": self.welcome_video.url,
            "years_of_experience": self.years_of_experience,
            "unique_scenarios": self.unique_scenarios,
            "implemented_projects": self.implemented_projects,
            "address": self.address_ru,
            "contact_phone": self.contact_phone,
            "contact_email": self.contact_email,
            "telegram": self.telegram,
            "ok": self.ok,
            "vk": self.vk,
            "email_for_clients": self.email_for_clients.split(","),
            "email_for_mass_media": self.email_for_mass_media,
            "email_for_partners": self.email_for_partners,
            "email_for_applicant": self.email_for_applicant,
            "portfolio": self.portfolio.url,
            "requisites": self.requisites.url,
            "presentation": self.presentation.url,
            "brief": self.brief.url,
            "agreement": self.agreement.url,
            "form_for_freelancers": self.form_for_freelancers.url,
        }

    @property
    def en(self):
        return {
            "greeting_title": self.greeting_title_en,
            "greeting_description": self.greeting_description_en,
            "about_image": self.about_image.url,
            "about_text": self.about_text_en,
            "intro_video": self.intro_video.url,
            "interview": self.interview.url,
            "welcome_video": self.welcome_video.url,
            "years_of_experience": self.years_of_experience,
            "unique_scenarios": self.unique_scenarios,
            "implemented_projects": self.implemented_projects,
            "address": self.address_en,
            "contact_phone": self.contact_phone,
            "contact_email": self.contact_email,
            "telegram": self.telegram,
            "ok": self.ok,
            "vk": self.vk,
            "email_for_clients": self.email_for_clients.split(","),
            "email_for_mass_media": self.email_for_mass_media,
            "email_for_partners": self.email_for_partners,
            "email_for_applicant": self.email_for_applicant,
            "portfolio": self.portfolio.url,
            "requisites": self.requisites.url,
            "presentation": self.presentation.url,
            "brief": self.brief.url,
            "agreement": self.agreement.url,
            "form_for_freelancers": self.form_for_freelancers.url,
        }


# class Fact(models.Model):
#     class Meta:
#         verbose_name = "Факт"
#         verbose_name_plural = "Факты"
#
#     number = models.SmallIntegerField(verbose_name="Число")
#     title = models.CharField(max_length=256, verbose_name="Описание")
#     company = models.ForeignKey(
#         "core.Company", on_delete=models.CASCADE, verbose_name="Факт о компании"
#     )
#
#     def __str__(self) -> str:
#         return f"Факт о {self.company.name}"


class TeamMember(models.Model):
    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Члены команды"

    name_ru = models.CharField(max_length=256, verbose_name="Имя (Ru)")
    name_en = models.CharField(max_length=256, verbose_name="Имя (En)")
    position_ru = models.CharField(
        max_length=256, verbose_name="Должность (Ru)"
    )
    position_en = models.CharField(
        max_length=256, verbose_name="Должность (En)"
    )
    photo = models.FileField(
        verbose_name="Фото",
        upload_to=upload_path,
    )
    is_chief = models.BooleanField(verbose_name="Руководитель?", default=False)

    def __str__(self) -> str:
        return f"Сотрудник {self.name_ru}"

    @property
    def ru(self):
        return {
            "id": self.id,
            "name": self.name_ru,
            "position": self.position_ru,
            "photo": self.photo.url,
            "is_chief": self.is_chief,
        }

    @property
    def en(self):
        return {
            "id": self.id,
            "name": self.name_en,
            "position": self.position_en,
            "photo": self.photo.url,
            "is_chief": self.is_chief,
        }


class GalleryAttachment(models.Model):
    class Meta:
        verbose_name = "Вложение галереи"
        verbose_name_plural = "Вложения галереи"

    title = models.CharField(max_length=256, verbose_name="Название")
    image = models.FileField(
        verbose_name="Изображение",
        upload_to=upload_path,
    )

    def __str__(self) -> str:
        return f"Вложение галерей {self.title}"


class Award(models.Model):
    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"

    year = models.PositiveIntegerField(verbose_name="Год")
    title_ru = models.CharField(max_length=256, verbose_name="Название (Ru)")
    title_en = models.CharField(max_length=256, verbose_name="Название (En)")
    place_ru = models.CharField(max_length=256, verbose_name="Место (Ru)", null=True)
    place_en = models.CharField(max_length=256, verbose_name="Место (En)", null=True)
    nomination_ru = models.CharField(
        max_length=256, verbose_name="Номинация (Ru)"
    )
    nomination_en = models.CharField(
        max_length=256, verbose_name="Номинация (En)"
    )
    event_ru = models.CharField(max_length=256, verbose_name="Мероприятие")
    event_en = models.CharField(max_length=256, verbose_name="Мероприятие (En)", null=True)
    case = models.ForeignKey("blog.Case", verbose_name="Кейс", null=True, on_delete=models.CASCADE)

    attachment = models.FileField(
        verbose_name="ЗD модель награды",
        upload_to=upload_path,
    )
    show_on_main_page = models.BooleanField(
        verbose_name="Показывать на главной странице", default=False
    )
    award_order = models.IntegerField(verbose_name="Порядковый номер награды", default=1)

    def __str__(self) -> str:
        return f"Награда {self.title_ru}"

    @property
    def ru(self):
        return {
            "id": self.id,
            "year": self.year,
            "title": self.title_ru,
            "place": self.place_ru,
            "nomination": self.nomination_ru,
            "event": self.event_ru,
            "attachment": self.attachment.url,
            "show_on_main_page": self.show_on_main_page,
            "award_order": self.award_order,
            "case_id": self.case_id,
        }

    @property
    def en(self):
        return {
            "id": self.id,
            "year": self.year,
            "title": self.title_en,
            "place": self.place_en,
            "nomination": self.nomination_en,
            "event": self.event_en,
            "attachment": self.attachment.url,
            "show_on_main_page": self.show_on_main_page,
            "award_order": self.award_order,
            "case_id": self.case_id,
        }
