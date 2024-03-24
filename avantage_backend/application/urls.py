from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django_serializer.v2.swagger.views import index as swagger_index


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(
            [
                path("swagger.json", swagger_index),
                path(
                    "bids.",
                    include("avantage_backend.bids.urls"),
                ),
                path(
                    "blog.",
                    include("avantage_backend.blog.urls"),
                ),
                path(
                    "cooperation.",
                    include("avantage_backend.cooperation.urls"),
                ),
                path(
                    "core.",
                    include("avantage_backend.core.urls"),
                ),
                path(
                    "goods.",
                    include("avantage_backend.goods.urls"),
                ),
                path(
                    "wiki.",
                    include("avantage_backend.wiki.urls"),
                ),
            ]
        ),
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
else:
    urlpatterns += [
        re_path(
            f"^{settings.MEDIA_URL.lstrip('/')}(?P<path>.*)$",
            serve,
            {"document_root": settings.MEDIA_ROOT},
        ),
        re_path(
            f"^{settings.STATIC_URL.lstrip('/')}(?P<path>.*)$",
            serve,
            {"document_root": settings.STATIC_ROOT},
        ),
    ]

if settings.SILK:
    urlpatterns += [
        re_path(r"silk/", include("silk.urls", namespace="silk")),
    ]
