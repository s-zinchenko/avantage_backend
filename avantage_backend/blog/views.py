from django.shortcuts import render
from django_serializer.v2.views import ListApiView, GetApiView

from avantage_backend.blog.forms import GetCaseListViewForm, GetCaseViewForm
from avantage_backend.blog.models import Article, Case
from avantage_backend.blog.serializers import ArticleSerializer, CaseSerializer
from avantage_backend.share.forms import LangForm


class GetArticleListView(ListApiView):
    class Meta:
        model = Article
        query_form = LangForm
        serializer = ArticleSerializer
        tags = ["blog"]


class GetCaseListView(ListApiView):
    class Meta:
        model = Case
        serializer = CaseSerializer
        query_form = GetCaseListViewForm
        tags = ["blog"]

    def get_queryset(self):
        queryset = (
            super()
            .get_queryset()
            .select_related("customer")
            .prefetch_related("caseattachment_set")
        )
        if case_type := self.request_query["case_type"]:
            queryset = queryset.filter(type_en=case_type)
        if show_on_main_page := self.request_query["show_on_main_page"]:
            queryset = queryset.filter(show_on_main_page=show_on_main_page)
        return queryset


class GetCaseView(GetApiView):
    class Meta:
        model = Case
        query_form = GetCaseViewForm
        serializer = CaseSerializer
        tags = ["blog"]

    def get_object(self):
        m = self.Meta.model
        key: str = self.Meta.object_key
        return (
            m.objects.select_related("customer")
            .prefetch_related("caseattachment_set")
            .get(**{key: self.request_query[key]})
        )
