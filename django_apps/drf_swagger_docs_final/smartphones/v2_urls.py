from rest_framework.routers import DefaultRouter
from .views import PhoneV2ViewSet
from django.urls import path, include

router = DefaultRouter()

router.register("", PhoneV2ViewSet, basename="phones")

urlpatterns = [
    path("", include(router.urls)),
]
