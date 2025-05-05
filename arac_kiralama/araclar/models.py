from django.db import models
from django.contrib.auth.models import User


class Arac(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    plaka = models.CharField(max_length=20, unique=True)
    gunluk_fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    uygun_mu = models.BooleanField(default=True)
    resim = models.ImageField(upload_to='arac_resimleri/', null=True, blank=True)  # ✅ Fotoğraf alanı

    def __str__(self):
        return f"{self.marka} {self.model} ({self.plaka})"


class Musteri(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  # Opsiyonel kalsın

def __str__(self):
    full_name = f"{self.ad or ''} {self.soyad or ''}"
    return full_name.strip()



class Rezervasyon(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE)
    arac = models.ForeignKey(Arac, on_delete=models.CASCADE)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()

    def __str__(self):
        return f"{self.musteri} -> {self.arac} ({self.baslangic_tarihi} - {self.bitis_tarihi})"
