from django.urls import path
from avantage_backend.core.views import (
    AboutCompanyView,
    GetCompanyFilesView,
    GetTeamMemberListView,
    GetGalleryView,
    GetAwardsListView,
    GetCompanyContactsView,
)

urlpatterns = [
    path("about", AboutCompanyView.as_view()),
    path("files", GetCompanyFilesView.as_view()),
    path("contacts", GetCompanyContactsView.as_view()),
    path("team", GetTeamMemberListView.as_view()),
    path("gallery", GetGalleryView.as_view()),
    path("awards_list", GetAwardsListView.as_view()),
]
