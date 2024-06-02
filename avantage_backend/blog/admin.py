from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from avantage_backend.blog.forms import ValidateShowOnMainPageFormset
from avantage_backend.blog.models import Article, Case, Customer, CaseAttachment


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


class CaseAttachmentInlineAdmin(admin.TabularInline):
    model = CaseAttachment
    formset = ValidateShowOnMainPageFormset


@admin.register(Article)
class ArticleAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = [
        "id",
        "title_ru",
    ]


@admin.register(Case)
class CaseAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = [
        "id",
        "title_ru",
        "year",
    ]
    inlines = [
        CaseAttachmentInlineAdmin,
    ]
