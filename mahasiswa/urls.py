from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='daftar/')),
    path('daftar/', views.daftar_mahasiswa, name='daftar_mahasiswa'),
]