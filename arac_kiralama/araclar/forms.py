from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Rezervasyon, Musteri

# ✅ Rezervasyon Formu
class RezervasyonForm(forms.ModelForm):
    class Meta:
        model = Rezervasyon
        fields = ['arac', 'baslangic_tarihi', 'bitis_tarihi']
        widgets = {
            'baslangic_tarihi': forms.DateInput(attrs={'type': 'date'}),
            'bitis_tarihi': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 'musteri' formda görünmüyor çünkü giriş yapan kullanıcıya göre set ediliyor

# ✅ Özel Kullanıcı Oluşturma Formu (Kayıt ekranı için)
class CustomUserCreationForm(UserCreationForm):
    ad = forms.CharField(max_length=50, label='Adınız')
    soyad = forms.CharField(max_length=50, label='Soyadınız')
    email = forms.EmailField(label='E-posta')
    telefon = forms.CharField(max_length=20, label='Telefon Numaranız')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'ad', 'soyad', 'telefon']

