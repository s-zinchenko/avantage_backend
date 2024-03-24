from django.db.models import Prefetch
from django_serializer.v2.views import ListApiView

from avantage_backend.wiki.models import Letter, Record
from avantage_backend.wiki.serializers import WikiSerializer


class WikiView(ListApiView):
    class Meta:
        model = Letter
        serializer = WikiSerializer
        tags = ["wiki"]

    def get_queryset(self):
        qs = (
            super()
            .get_queryset()
            .prefetch_related(
                Prefetch("record_set", Record.objects.all().order_by("title"))
            )
            .order_by("value")
        )
        return qs
