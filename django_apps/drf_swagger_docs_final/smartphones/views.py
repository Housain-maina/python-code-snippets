from .serializers import PhoneSerializer
from .models import Phone
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(list=extend_schema(description="List of smartphones."))
class PhoneViewSet(GenericViewSet, ListModelMixin):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneV2ViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

    @extend_schema(description="List of smartphones.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(description="Retrieve a smartphone.")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
