from django.urls import path
from . import views 

urlpatterns = [
    path('', views.danh_sach_sinh_vien, name='danh_sach_sinh_vien'),
    path('them_sinh_vien/', views.them_sinh_vien, name='them_sinh_vien'),
    path('danh_sach_mon_hoc/', views.danh_sach_mon_hoc, name='danh_sach_mon_hoc'),
    path('them_mon_hoc/', views.them_mon_hoc, name='them_mon_hoc'),
    path('diem_sinh_vien/', views.diem_sinh_vien, name='diem_sinh_vien'),
    path('them_diem/', views.them_diem, name='them_diem'),
    path('xoa_sinh_vien/<int:sinh_vien_id>/', views.xoa_sinh_vien, name='xoa_sinh_vien'),
    path('xoa_mon_hoc/<int:mon_hoc_id>/', views.xoa_mon_hoc, name='xoa_mon_hoc'),
]
