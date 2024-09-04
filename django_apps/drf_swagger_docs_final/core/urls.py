from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularJSONAPIView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("schema.json", SpectacularJSONAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("v1/smartphones/", include("smartphones.v1_urls")),
    path("v2/smartphones/", include("smartphones.v2_urls")),
]
