from rest_framework import generics  # Django REST Framework'ü import et
from rest_framework import status
from rest_framework.response import Response
from .models import Ihtiyac
from .serializers import IhtiyacListCrateSerializer


class IhtiyacListCreateView(generics.ListCreateAPIView):
    serializer_class = IhtiyacListCrateSerializer

    def get_queryset(self):
        return Ihtiyac.actives.by_user(self.request.user)


class IhtiyacListFilterByCityView(generics.ListAPIView):
    serializer_class = IhtiyacListCrateSerializer

    def get_queryset(self):
        return Ihtiyac.objects.filter(city=self.request.user.city)


class IhtiyacRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IhtiyacListCrateSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Ihtiyac.actives.by_user(self.request.user)


# views.py dosyasında
from django.http import JsonResponse
import requests


def ihtiyac_listesi_view(request):
    api_url = "http://localhost:8000/api/ihtiyaclar/"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            veri = response.json()
            return JsonResponse(veri)
        else:
            return JsonResponse(
                {
                    "error": "API isteği başarısız. Status Code: {}".format(
                        response.status_code
                    )
                }
            )
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": "Hata Oluştu: {}".format(str(e))})
