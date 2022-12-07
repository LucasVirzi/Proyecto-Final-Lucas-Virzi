from django.contrib import admin
from django.urls import path
from app_proyecto.views import index, saludar_a, sumar, monstrar_familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar_a/<nombre>', saludar_a),
    path('sumar/<int:a>/<int:b>', sumar),
    path('mi-familia/', monstrar_familiares),
]