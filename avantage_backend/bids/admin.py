from django.contrib import admin

from avantage_backend.bids.models import CooperationBid


@admin.register(CooperationBid)
class CooperationBidAdmin(admin.ModelAdmin):
    pass
