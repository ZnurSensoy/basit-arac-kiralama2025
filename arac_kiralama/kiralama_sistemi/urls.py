from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👇 araclar uygulamasındaki URL'leri dahil ediyoruz
    path('', include('araclar.urls')),

    # 👇 Giriş ve çıkış işlemleri (auth_views ile)
    path('giris/', auth_views.LoginView.as_view(template_name='registration/giris.html'), name='giris'),
    path('cikis/', auth_views.LogoutView.as_view(next_page='/giris/'), name='cikis'),
]

# 👇 Resim dosyalarını gösterebilmek için:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
