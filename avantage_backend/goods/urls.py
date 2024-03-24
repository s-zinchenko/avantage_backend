from django.urls import path

from avantage_backend.goods.views import ProductsListView

urlpatterns = [path("list", ProductsListView.as_view())]
