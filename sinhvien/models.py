from django.db import models

class SinhVien(models.Model):
    ma_sv = models.CharField(max_length=12, unique=True)
    ho_ten = models.CharField(max_length=100)
    nien_khoa = models.CharField(max_length=9)

    def __str__(self):
        return self.ho_ten

class MonHoc(models.Model):
    ma_mon = models.CharField(max_length=10, unique=True)
    ten_mon = models.CharField(max_length=100)
    so_tin_chi = models.IntegerField()

    def tinh_hoc_phi(self):
        return self.so_tin_chi * 850

    def __str__(self):
        return self.ten_mon

class Diem(models.Model):
    sinh_vien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
    mon_hoc = models.ForeignKey(MonHoc, on_delete=models.CASCADE)
    diem = models.FloatField()

    def __str__(self):
        return f"{self.sinh_vien.ho_ten} - {self.mon_hoc.ten_mon}: {self.diem}"
