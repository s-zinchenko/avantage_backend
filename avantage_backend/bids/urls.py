from django.urls import path

from avantage_backend.bids.views import (
    CooperationBidCreateView,
)

urlpatterns = [
    path("cooperation.create", CooperationBidCreateView.as_view()),
]
