from django.urls import path

from avantage_backend.cooperation.views import (
    PartnersListView,
    RatingsListView,
)

urlpatterns = [
    path("partners.list", PartnersListView.as_view()),
    path("ratings.list", RatingsListView.as_view()),
]
