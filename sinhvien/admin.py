from django.contrib import admin
from .models import SinhVien, MonHoc

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['ma_sv', 'ho_ten', 'nien_khoa']
    search_fields = ['ma_sv', 'ho_ten']
admin.site.register(SinhVien, PostAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['ma_mon', 'ten_mon', 'so_tin_chi']
    search_fields = ['ma_mon', 'ten_mon']
admin.site.register(MonHoc, PostAdmin)
