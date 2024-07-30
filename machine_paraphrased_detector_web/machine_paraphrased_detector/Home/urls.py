# import library
from django.urls import path, re_path

# import file views
from . import views


urlpatterns=[
    path('', views.index), # untuk menampilkan halaman utama
]