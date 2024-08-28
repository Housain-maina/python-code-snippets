from django.shortcuts import render
from .serializers import PhoneSerializer
from .models import Phone
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin


class PhoneViewSet(GenericViewSet, ListModelMixin):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
