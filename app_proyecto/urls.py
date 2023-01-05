from django.contrib import admin
from django.urls import path
from app_proyecto.views import (index, saludar_a, sumar, mostrar_familiares, BuscarFamiliar,
 AltaFamiliar, ActualizarFamiliar, BorrarFamiliar)

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
]