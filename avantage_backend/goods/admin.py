from django.contrib import admin

from avantage_backend.goods.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
