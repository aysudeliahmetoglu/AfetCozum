# urls.py
from django.urls import path
from .views import DonationListCreateAPIView, DonationRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('donations/', DonationListCreateAPIView.as_view(), name='donation-list-create'),
    path('donations/<int:pk>/', DonationRetrieveUpdateDestroyAPIView.as_view(), name='donation-detail'),
]
