from django.shortcuts import render
from django.views.generic import ListView, CreateView
from app_2.models import Post
from django.urls import reverse_lazy

def index(request):
    return render(request, "app_2/index.html", {})
    
class PostList (ListView):
    model = Post        

class PostCrear(CreateView):
    model = Post        
    succes_url = "/app_2/listar"
    fields = '__all__'