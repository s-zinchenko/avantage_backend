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
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title_ru",
        "article_order",
    ]


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title_ru",
        "year",
        "case_order",
    ]
    inlines = [
        CaseAttachmentInlineAdmin,
    ]
