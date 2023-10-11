from django.db import models

from need_api.models import Ihtiyac

# Create your models here.


class IhtiyacForm(models.Model):
    class NeedCategory(models.TextChoices):
        A = "Temel İhtiyaçlar"
        B = "Sağlık Hizmetleri"
        C = "Psikososyal Destek"
        D = "Maddi Destek"

    ad_soyad = models.CharField(max_length=100)  # Ihtiyacın adı
    telefon = models.CharField(max_length=100, null=True, blank=True)  # Ihtiyacın adı
    ihtiyaç_kategorisi = models.CharField(
        max_length=100, choices=NeedCategory.choices, null=True, blank=True
    )  # Ihtiyacın adı
    adres = models.TextField()  # Ihtiyacın açıklaması
    email = models.PositiveIntegerField(default=0)  # Stok miktarı
    ihtiyac = models.OneToOneField(Ihtiyac, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ad_soyad} - {self.id}"
