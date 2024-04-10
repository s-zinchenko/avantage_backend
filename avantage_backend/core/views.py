from typing import Any, Dict

from django.core.handlers.wsgi import WSGIRequest
from django_serializer.v2.views import ApiView, HttpMethod, ListApiView

from avantage_backend.core.forms import GetAwardsListForm, GetTeamListForm
from avantage_backend.core.models import (
    Company,
    TeamMember,
    GalleryAttachment,
    Award,
)
from avantage_backend.core.serializers import (
    AboutCompanySerializer,
    TeamMemberSerializer,
    GalleryAttachmentSerializer,
    AwardSerializer,
    GetCompanyFilesSerializer,
    GetCompanyContactsSerializer,
)
from avantage_backend.share.forms import LangForm


class AboutCompanyView(ApiView):
    class Meta:
        model = Company
        method = HttpMethod.GET
        query_form = LangForm
        serializer = AboutCompanySerializer
        tags = ["core"]

    def execute(
        self, request: WSGIRequest, *args: Any, **kwargs: Dict[Any, Any]
    ) -> Dict[Any, Any]:
        obj = Company.objects.get()
        return obj


class GetCompanyFilesView(ApiView):
    class Meta:
        model = Company
        method = HttpMethod.GET
        serializer = GetCompanyFilesSerializer
        tags = ["core"]

    def execute(
        self, request: WSGIRequest, *args: Any, **kwargs: Dict[Any, Any]
    ) -> Dict[Any, Any]:
        obj = Company.objects.get()
        return obj


class GetCompanyContactsView(ApiView):
    class Meta:
        model = Company
        method = HttpMethod.GET
        query_form = LangForm
        serializer = GetCompanyContactsSerializer
        tags = ["core"]

    def execute(
        self, request: WSGIRequest, *args: Any, **kwargs: Dict[Any, Any]
    ) -> Dict[Any, Any]:
        obj = Company.objects.get()
        return obj


class GetTeamMemberListView(ListApiView):
    class Meta:
        model = TeamMember
        query_form = GetTeamListForm
        serializer = TeamMemberSerializer
        tags = ["core"]

    def get_queryset(self):
        queryset = super().get_queryset()
        is_chief = self.request_query.get("is_chief")
        if is_chief is not None:
            queryset = queryset.filter(is_chief=is_chief)

        return queryset


class GetGalleryView(ListApiView):
    class Meta:
        model = GalleryAttachment
        serializer = GalleryAttachmentSerializer
        tags = ["core"]


class GetAwardsListView(ListApiView):
    class Meta:
        model = Award
        query_form = GetAwardsListForm
        serializer = AwardSerializer
        tags = ["core"]

    def get_queryset(self):
        queryset = super().get_queryset()
        if show_on_main_page := self.request_query["show_on_main_page"]:
            queryset = queryset.filter(show_on_main_page=show_on_main_page)
        return queryset
