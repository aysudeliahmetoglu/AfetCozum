from django.urls import path
from .views import (
    IhtiyacListCreateView,
    IhtiyacListFilterByCityView,
    IhtiyacRetrieveUpdateDestroyAPIView,
    ihtiyac_listesi_view,
)

urlpatterns = [
    path("ihtiyaclar/", IhtiyacListCreateView.as_view(), name="ihtiyac-list-create"),
    path(
        "ihtiyaclar-by-city/",
        IhtiyacListFilterByCityView.as_view(),
        name="ihtiyac-filter-by-city",
    ),
    path(
        "ihtiyaclar/<int:id>",
        IhtiyacRetrieveUpdateDestroyAPIView.as_view(),
        name="ihtiyac-update",
    ),
    path("ihtiyac-listesi/", ihtiyac_listesi_view, name="ihtiyac-listesi"),
]
