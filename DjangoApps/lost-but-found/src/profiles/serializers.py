from rest_framework import serializers
from djoser.serializers import UserSerializer
from .models import Profile


class ProfileGetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"


class ProfilePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["user", "id"]
