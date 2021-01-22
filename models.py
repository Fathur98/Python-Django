from django.db import models

class Karyawan(models.Model):  
    nik = models.CharField(max_length=15)
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)