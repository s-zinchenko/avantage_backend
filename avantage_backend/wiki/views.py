from collections import defaultdict

from django.db.models import Prefetch
from django_serializer.v2.views import ListApiView

from avantage_backend.share.forms import LangForm
from avantage_backend.wiki.models import Letter, Record
from avantage_backend.wiki.serializers import WikiSerializer


class WikiView(ListApiView):
    class Meta:
        model = Letter
        query_form = LangForm
        serializer = WikiSerializer
        tags = ["wiki"]

    def get_queryset(self):
        qs = (
            super()
            .get_queryset()
            .filter(site_lang=self.request_query["lang"])
            .prefetch_related(
                Prefetch("record_set", Record.objects.all().order_by("title"))
            )
            .order_by("value")
        )
        return qs

    # def execute(self, request, *args, **kwargs):
    #     qs = super().execute(request, *args, **kwargs)
    #     res = dict.fromkeys(Letter.Lang.values, [])
    #     for letter in qs:
    #         if letter.lang:
    #             lang = letter.lang
    #         else:
    #             lang = Letter.Lang.RU
    #
    #         res[lang].append(letter)
    #
    #     return {"records":res}
