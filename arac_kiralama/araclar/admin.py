from django.contrib import admin
from .models import Arac, Musteri, Rezervasyon

@admin.register(Musteri)
class MusteriAdmin(admin.ModelAdmin):
    list_display = ('ad', 'soyad', 'email', 'telefon', 'user')
    search_fields = ('ad', 'soyad', 'email')
    list_filter = ('ad',)

admin.site.register(Arac)
admin.site.register(Rezervasyon)
