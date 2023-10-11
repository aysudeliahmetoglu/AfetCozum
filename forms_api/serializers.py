# ihtiyac/serializers.py
from rest_framework import serializers
from need_api.models import Ihtiyac

from need_api.serializers import IhtiyacListCrateSerializer
from forms_api.models import IhtiyacForm


class IhtiyacFormCreateListSerializer(serializers.ModelSerializer):
    ihtiyac = IhtiyacListCrateSerializer(many=False)

    class Meta:
        model = IhtiyacForm
        fields = (
            "id",
            "ad_soyad",
            "telefon",
            "ihtiyaç_kategorisi",
            "adres",
            "email",
            "ihtiyac",
        )

    def create(self, validated_data):
        ihtiyac_data = validated_data.pop("ihtiyac")
        ihtiyac_instance = Ihtiyac.objects.create(**ihtiyac_data)
        profile_instance = IhtiyacForm.objects.create(
            ihtiyac=ihtiyac_instance, **validated_data
        )
        return profile_instance
