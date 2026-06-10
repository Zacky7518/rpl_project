from django.shortcuts import render, redirect, get_object_or_404
from .models import Mahasiswa
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'judul': 'Halo Mahasiswa',
        'deskripsi': 'Contoh halaman index menggunakan Django templates dan static files.'
    }
    return render(request, 'mahasiswa/index.html', context)

@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()
    return render(request, 'mahasiswa/daftar.html', {'mahasiswas': mahasiswas})

@login_required(login_url='/accounts/login/')
def tambah_mahasiswa(request):
    if request.method == 'POST':
        nim = request.POST.get('nim')
        nama = request.POST.get('nama')
        programstudi = request.POST.get('programstudi')
        angkatan = request.POST.get('angkatan')
        Mahasiswa.objects.create(nim=nim, nama=nama, programstudi=programstudi, angkatan=angkatan)
        return redirect('daftar_mahasiswa')
    return render(request, 'mahasiswa/tambah.html')

@login_required(login_url='/accounts/login/')
def edit_mahasiswa(request, id):
    mhs = get_object_or_404(Mahasiswa, id=id)
    if request.method == 'POST':
        mhs.nim = request.POST.get('nim')
        mhs.nama = request.POST.get('nama')
        mhs.programstudi = request.POST.get('programstudi')
        mhs.angkatan = request.POST.get('angkatan')
        mhs.save()
        return redirect('daftar_mahasiswa')
    return render(request, 'mahasiswa/edit.html', {'mhs': mhs})

@login_required(login_url='/accounts/login/')
def hapus_mahasiswa(request, id):
    mhs = get_object_or_404(Mahasiswa, id=id)
    mhs.delete()
    return redirect('daftar_mahasiswa')