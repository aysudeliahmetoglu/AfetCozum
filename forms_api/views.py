from rest_framework import generics

from forms_api.models import IhtiyacForm
from forms_api.serializers import (
    IhtiyacFormCreateListSerializer,
)  # Django REST Framework'ü import et


class IhtiyacFormCreateListView(generics.ListCreateAPIView):
    queryset = IhtiyacForm.objects.all()
    serializer_class = IhtiyacFormCreateListSerializer
