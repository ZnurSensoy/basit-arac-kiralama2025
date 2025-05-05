from django.urls import path
from . import views

urlpatterns = [
    # Ana sayfa yönlendirme (boş dizin)
    path('', views.arac_listesi, name='arac_listesi'),

    # Araç listesi
    path('araclar/', views.arac_listesi, name='arac_listesi'),

    # Rezervasyon
    path('rezervasyon/', views.rezervasyon_yap, name='rezervasyon_yap'),

    # Giriş, çıkış ve kayıt ol
    path('giris/', views.giris, name='giris'),
    path('cikis/', views.cikis, name='cikis'),
    path('kayit/', views.kayit_ol, name='kayit_ol'),

    # ✅ Araç detay sayfası (EKLENDİ)
    path('arac/<int:arac_id>/', views.arac_detay, name='arac_detay'),
]
