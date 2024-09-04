from rest_framework.routers import DefaultRouter
from .views import PhoneViewSet
from django.urls import path, include

router = DefaultRouter()

router.register("", PhoneViewSet, basename="phones")

urlpatterns = [path("", include(router.urls))]
