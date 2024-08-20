from django.shortcuts import render, get_object_or_404, redirect
from .models import SinhVien, MonHoc, Diem
from .forms import SinhVienForm, MonHocForm, DiemForm

def danh_sach_sinh_vien(request):
    sinh_viens = SinhVien.objects.all()
    return render(request, 'page/danh_sach_sinh_vien.html', {'sinh_viens': sinh_viens})

def them_sinh_vien(request):
    if request.method == 'POST':
        form = SinhVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_sinh_vien')
    else:
        form = SinhVienForm()
    return render(request, 'page/them_sinh_vien.html', {'form': form})

def danh_sach_mon_hoc(request):
    mon_hocs = MonHoc.objects.all()
    return render(request, 'page/danh_sach_mon_hoc.html', {'mon_hocs': mon_hocs})

def them_mon_hoc(request):
    if request.method == 'POST':
        form = MonHocForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_mon_hoc')
    else:
        form = MonHocForm()
    return render(request, 'page/them_mon_hoc.html', {'form': form})

def diem_sinh_vien(request):
    diems = Diem.objects.all()
    return render(request, 'page/diem_sinh_vien.html', {'diems': diems})

def them_diem(request):
    if request.method == 'POST':
        form = DiemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diem_sinh_vien')
    else:
        form = DiemForm()
    return render(request, 'page/them_diem.html', {'form': form})


def xoa_sinh_vien(request, sinh_vien_id):
    sinh_vien = get_object_or_404(SinhVien, pk=sinh_vien_id)
    if request.method == 'POST':
        sinh_vien.delete()
        return redirect('danh_sach_sinh_vien')
    return render(request, 'pages/xoa_sinh_vien.html', {'sinh_vien': sinh_vien})

def xoa_mon_hoc(request, mon_hoc_id):
    mon_hoc = get_object_or_404(MonHoc, pk=mon_hoc_id)
    if request.method == 'POST':
        mon_hoc.delete()
        return redirect('danh_sach_mon_hoc')
    return render(request, 'pages/xoa_mon_hoc.html', {'mon_hoc': mon_hoc})
