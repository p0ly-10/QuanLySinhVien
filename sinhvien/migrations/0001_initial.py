# Generated by Django 5.0.4 on 2024-05-22 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonHoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_mon', models.CharField(max_length=10, unique=True)),
                ('ten_mon', models.CharField(max_length=100)),
                ('so_tin_chi', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_sv', models.CharField(max_length=12, unique=True)),
                ('ho_ten', models.CharField(max_length=100)),
                ('nien_khoa', models.CharField(max_length=9)),
            ],
        ),
    ]
