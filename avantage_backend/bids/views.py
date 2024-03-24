from typing import Any, Dict

from django.core.handlers.wsgi import WSGIRequest
from django_serializer.v2.serializer import Serializer
from django_serializer.v2.views import CreateApiView

from avantage_backend.bids.forms import CooperationBidCreateForm
from avantage_backend.bids.models import CooperationBid


class CooperationBidCreateView(CreateApiView):
    class Meta:
        model = CooperationBid
        model_form = CooperationBidCreateForm
        serializer = Serializer
        tags = ["bids"]

    def execute(
        self, request: WSGIRequest, *args: Any, **kwargs: Dict[Any, Any]
    ):
        obj = super().execute(request, *args, **kwargs)
        # obj.send_email()
        return obj
