# ihtiyac/serializers.py
from rest_framework import serializers
from .models import Ihtiyac


class IhtiyacListCrateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ihtiyac
        fields = ("id", "name", "description", "stock", "city", "user")


class IhtiyacListCrateSerializer(serializers.ModelSerializer):
    user = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ihtiyac
        fields = ("id", "name", "description", "stock", "city", "user")
