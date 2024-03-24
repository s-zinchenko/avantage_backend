from django_serializer.v2.views import ListApiView

from avantage_backend.goods.models import Product
from avantage_backend.goods.serializers import ProductSerializer
from avantage_backend.share.forms import LangForm


class ProductsListView(ListApiView):
    class Meta:
        model = Product
        tags = ["catalog"]
        query_form = LangForm
        serializer = ProductSerializer
        ordering = ("order",)
