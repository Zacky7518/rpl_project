from django.shortcuts import render
from .models import Mahasiswa
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    # Mengambil semua data mahasiswa dari database untuk dikirim ke template
    mahasiswas = Mahasiswa.objects.all()
    return render(request, 'mahasiswa/daftar.html', {'mahasiswas': mahasiswas})