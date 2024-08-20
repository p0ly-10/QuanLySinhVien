from django import forms
from .models import SinhVien, MonHoc, Diem

class SinhVienForm(forms.ModelForm):
    class Meta:
        model = SinhVien
        fields = ['ma_sv', 'ho_ten', 'nien_khoa']

class MonHocForm(forms.ModelForm):
    class Meta:
        model = MonHoc
        fields = ['ma_mon', 'ten_mon', 'so_tin_chi']

class DiemForm(forms.ModelForm):
    class Meta:
        model = Diem
        fields = ['sinh_vien', 'mon_hoc', 'diem']
