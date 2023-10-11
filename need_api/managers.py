from django.db.models import Manager
from django.db.models.query import QuerySet


class IhtiyacManager(Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()

    def by_user(self, user):
        return self.filter(user=user)
