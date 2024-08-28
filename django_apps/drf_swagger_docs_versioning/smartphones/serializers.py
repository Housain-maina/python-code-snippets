from .models import Phone
from rest_framework import serializers


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = "__all__"