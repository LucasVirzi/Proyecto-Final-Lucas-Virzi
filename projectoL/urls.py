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
 AltaFamiliar, ActualizarFamiliar, BorrarFamiliar)
from app_2.views import (index, PostList, PostCrear, PostDetalle, PostBorrar, PostActualizar, UserView,
 UserLogin, UserLogout, AvatarActualizar, UserActualizar,MensajeCrear, MensajeListar, MensajeDetalle)
from django.contrib.admin.views.decorators import  staff_member_required
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
    path('app_2/crear/', staff_member_required(PostCrear.as_view()), name = "app-2-crear"),
    path('app-2/<int:pk>/detalle/', PostDetalle.as_view(), name = "app-2-detalle"),
    path('app-2/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name = "app-2-borrar"),
    path('app-2/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name = "app-2-actualizar"),
    path('app_2/signup/', UserView.as_view(), name = "app-2-signup"),
    path('app_2/login/', UserLogin.as_view(), name = "app-2-login"),
    path('app_2/logout/', UserLogout.as_view(), name = "app-2-logout"),
    path('app-2/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name = "app-2-avatars-actualizar"),
    path('app-2/users/<int:pk>/actualizar/', UserActualizar.as_view(), name = "app-2-users-actualizar"),
    path('app-2/mensajes/crear/', MensajeCrear.as_view(), name = "app-2-mensajes-crear"),
    path('app-2/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name = "app-2-mensajes-detalle"),
    path('app-2/mensajes/listar/', MensajeListar.as_view(), name = "app-2-mensajes-listar"),
]

urlpatterns += staticfiles_urlpatterns()