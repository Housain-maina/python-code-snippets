from functools import partial
from .serializers import ProfileGetSerializer, ProfilePostSerializer
from .models import Profile
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status
from custom.permissions import IsProfileOwner
from custom.mixins import SerializerByMethodMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


class ProfileRetrieveUpdateViewSet(SerializerByMethodMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_map = {
        "GET": ProfileGetSerializer,
        "PUT": ProfilePostSerializer,
        "PATCH": ProfilePostSerializer,
    }
    permission_classes = [IsProfileOwner]

    def retrieve(self, request, pk=None):
        queryset = Profile.objects.all()
        profile = get_object_or_404(queryset, pk=request.user.id)
        serializer = ProfileGetSerializer(profile)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Profile.objects.all()
        profile = get_object_or_404(queryset, pk=request.user.id)
        serializer = ProfilePostSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
