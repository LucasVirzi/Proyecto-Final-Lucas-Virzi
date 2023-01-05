from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from app_2.models import Avatar, Post, Mensaje
from django.urls import reverse_lazy
from app_2.forms import UsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User

@login_required
def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, "app_2/index.html", {"posts":posts})
    
class PostList (LoginRequiredMixin, ListView):
    model = Post        

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post        
    succes_url = reverse_lazy("/app_2/listar")
    fields = '__all__'

class PostDetalle(DetailView):
    model = Post

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    succes_url = reverse_lazy("/app_2/listar")

class PostActualizar(UpdateView):
    model = Post
    succes_url = reverse_lazy("/app_2/listar")

class UserView(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    succes_url = reverse_lazy("/app_2/listar")

class UserLogin(LoginView):
    next_page = reverse_lazy("/app_2/listar")

class UserLogout(LogoutView):
    next_page = reverse_lazy("/app_2/listar")

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy("/app_2/listar")

class UserActualizar(UpdateView):
    model = User
    fields = ['firs_name', 'las_name', 'email']
    success_url = reverse_lazy("/app_2/listar")

class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("app-2-mensajes-crear")
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("app-2-mensajes-listar")
