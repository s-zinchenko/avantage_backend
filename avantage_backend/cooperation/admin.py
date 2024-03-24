from django.contrib import admin

from avantage_backend.cooperation.models import (
    Partner,
    Rating,
)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass
