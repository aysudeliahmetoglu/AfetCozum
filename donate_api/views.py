# views.py
from rest_framework import generics
from .models import Donation
from .serializers import DonationSerializer

class DonationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer



class DonationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
