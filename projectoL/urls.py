"""projectoL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_proyecto.views import (index, saludar_a, sumar, mostrar_familiares, buscar, BuscarFamiliar,
 AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, mostrar_mascotas, AltaMascota, mostrar_autos,
 AltaAuto, ActualizarAuto, ActualizarMascota)
from app_2.views import (index, PostList, PostCrear)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar_a/<nombre>', saludar_a),
    path('sumar/<int:a>/<int:b>', sumar),
    path('mi-familia/', mostrar_familiares),
    path('buscar/', buscar),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('app_2/', index),
    path('app_2/listar/', PostList.as_view(), name = "app-2-listar"),
    path('app_2/crear/', PostCrear.as_view(), name = "app-2-crear"),
    path('mis-mascotas/', mostrar_mascotas),
    path('mis-mascotas/alta', AltaMascota.as_view()),
    path('mis-autos/', mostrar_autos),
    path('mis-autos/alta', AltaAuto.as_view()),
    path('mis-autos/actualizar/<int:pk>', ActualizarAuto.as_view()),
    path('mis-mascotas/actualizar/<int:pk>', ActualizarMascota.as_view()),
]
