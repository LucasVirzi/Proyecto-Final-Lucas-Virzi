from django.contrib import admin
from django.urls import path
from app_proyecto.views import (index, saludar_a, sumar, mostrar_familiares, BuscarFamiliar,
 AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, mostrar_mascotas, AltaMascota, mostrar_autos,
AltaAuto, ActualizarAuto, ActualizarMascota, BorrarMascota, BorrarAuto)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar_a/<nombre>', saludar_a),
    path('sumar/<int:a>/<int:b>', sumar),
    path('mi-familia/', mostrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('mis-mascotas/', mostrar_mascotas),
    path('mis-mascotas/alta', AltaMascota.as_view()),
    path('mis-autos/', mostrar_autos),
    path('mis-autos/alta', AltaAuto.as_view()),
    path('mis-autos/actualizar/<int:pk>', ActualizarAuto.as_view()),
    path('mis-mascotas/actualizar/<int:pk>', ActualizarMascota.as_view()),
    path('mis-mascotas/borrar/<int:pk>', BorrarMascota.as_view()),
    path('mis-autos/borrar/<int:pk>', BorrarAuto.as_view()),
]