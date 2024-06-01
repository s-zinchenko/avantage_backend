from django.contrib import admin
from solo.admin import SingletonModelAdmin

from avantage_backend.core.forms import AwardFormAdmin
from avantage_backend.core.models import (
    Company,
    TeamMember,
    GalleryAttachment,
    Award,
)


# class FactInline(admin.TabularInline):
#     model = Fact


@admin.register(Company)
class CompanyAdmin(SingletonModelAdmin):
    pass
    # inlines = [
    #     FactInline,
    # ]


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    pass


@admin.register(GalleryAttachment)
class GalleryAttachmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = (
        "title_ru",
        "show_on_main_page",
        "award_order",
    )
    form = AwardFormAdmin
