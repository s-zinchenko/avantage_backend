from django.urls import path

from avantage_backend.blog.views import (
    GetArticleListView,
    GetCaseListView,
    GetCaseView,
)

urlpatterns = [
    path("article_list", GetArticleListView.as_view()),
    path("case_list", GetCaseListView.as_view()),
    path("case", GetCaseView.as_view()),
]
