from django.db import models
from need_api.managers import IhtiyacManager

from user_api.models import AppUser
class Ihtiyac(models.Model):
    name = models.CharField(max_length=100)  # Ihtiyacın adı
    city = models.CharField(max_length=100, null=True, blank=True)  # Ihtiyacın adı
    description = models.TextField()  # Ihtiyacın açıklaması
    stock = models.PositiveIntegerField(default=0)  # Stok miktarı
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, blank=True, null=True)
    objects = models.Manager()
    actives = IhtiyacManager()
    def __str__(self):
        return self.name
