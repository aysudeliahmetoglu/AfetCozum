from django.urls import path

from forms_api.views import IhtiyacFormCreateListView


urlpatterns = [
    path("ihtiyac_form/", IhtiyacFormCreateListView.as_view(), name="ihtiyac-list-create"),
]
