# models.py
from django.db import models

from need_api.models import Ihtiyac


class Donation(models.Model):
    class DonationCategory(models.TextChoices):
        A = "Temel İhtiyaçlar"
        B = "Sağlık Hizmetleri"
        C = "Psikososyal Destek"
        D = "Maddi Destek"

    category = models.CharField(max_length=255, choices=DonationCategory.choices)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=255)
    ihtiyac = models.ForeignKey(Ihtiyac, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.id}"
