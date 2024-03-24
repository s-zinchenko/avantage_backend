from django.urls import path

from avantage_backend.wiki.views import WikiView

urlpatterns = [
    path("get", WikiView.as_view()),
]
