from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register("", views.ProfileRetrieveUpdateViewSet, basename="profile")


urlpatterns = [
    path("", include(router.urls)),
    path("me/", views.ProfileRetrieveUpdateViewSet.as_view({"get": "retrieve", "patch": "partial_update"})),
]
