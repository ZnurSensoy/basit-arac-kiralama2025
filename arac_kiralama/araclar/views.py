from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib import messages
from .forms import CustomUserCreationForm


from .forms import RezervasyonForm
from .models import Arac, Musteri, Rezervasyon


# 🚘 Araç listesi gösterimi
def arac_listesi(request):
    araclar = Arac.objects.filter(uygun_mu=True)
    return render(request, 'araclar/arac_listesi.html', {'araclar': araclar})


# 🛠 Araç detay sayfası
@login_required
def arac_detay(request, arac_id):
    arac = get_object_or_404(Arac, id=arac_id)
    return render(request, 'araclar/arac_detay.html', {'arac': arac})


# 📅 Rezervasyon yapma
@login_required
def rezervasyon_yap(request):
    if request.method == 'POST':
        form = RezervasyonForm(request.POST)
        if form.is_valid():
            rezervasyon = form.save(commit=False)
            musteri = get_object_or_404(Musteri, user=request.user)
            rezervasyon.musteri = musteri

            # ⛔ Geçmiş tarih kontrolü
            if rezervasyon.baslangic_tarihi < timezone.now().date():
                form.add_error('baslangic_tarihi', 'Geçmiş tarihe rezervasyon yapılamaz.')
            elif rezervasyon.bitis_tarihi < rezervasyon.baslangic_tarihi:
                form.add_error('bitis_tarihi', 'Bitiş tarihi, başlangıç tarihinden önce olamaz.')
            else:
                # ⛔ Çakışan rezervasyon kontrolü
                car_reservations = Rezervasyon.objects.filter(
                    arac=rezervasyon.arac,
                    bitis_tarihi__gte=rezervasyon.baslangic_tarihi,
                    baslangic_tarihi__lte=rezervasyon.bitis_tarihi
                )
                if car_reservations.exists():
                    form.add_error(None, 'Bu tarihlerde bu araç zaten rezerve edilmiş.')
                else:
                    rezervasyon.save()
                    return redirect('/araclar/')
    else:
        form = RezervasyonForm()
    return render(request, 'araclar/rezervasyon_formu.html', {'form': form})


# 🧾 Kayıt ol
@login_required
def kayit_ol(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            ad = form.cleaned_data['ad']
            soyad = form.cleaned_data['soyad']
            email = form.cleaned_data['email']
            telefon = form.cleaned_data['telefon']

            # Müşteri oluşturuluyor
            Musteri.objects.create(
                user=user,
                ad=ad,
                soyad=soyad,
                email=email,
                telefon=telefon
            )

            login(request, user)  # Otomatik giriş
            return redirect('arac_listesi')
    else:
        form = CustomUserCreationForm()
    return render(request, 'araclar/registration/kayit_ol.html', {'form': form})


# 🔐 Giriş yap
def giris(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('arac_listesi')
    else:
        form = AuthenticationForm()
    return render(request, 'araclar/registration/giris.html', {'form': form})


# 🔓 Çıkış yap
def cikis(request):
    logout(request)
    return redirect('giris')
