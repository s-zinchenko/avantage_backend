from django_serializer.v2.views import ListApiView

from avantage_backend.cooperation.models import (
    Partner,
    Rating,
)
from avantage_backend.cooperation.serializers import (
    PartnerItemSerializer,
    RatingItemSerializer,
)
from avantage_backend.share.forms import LangForm


class PartnersListView(ListApiView):
    class Meta:
        model = Partner
        query_form = LangForm
        serializer = PartnerItemSerializer
        tags = ["cooperation"]


class RatingsListView(ListApiView):
    class Meta:
        model = Rating
        query_form = LangForm
        serializer = RatingItemSerializer
        tags = ["cooperation"]
