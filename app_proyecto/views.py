from django import views
from django.shortcuts import render
from app_proyecto.models import Familiar
from app_proyecto.forms import Buscar
from django.views import View



def index(request):
    return render(request, "app_proyecto/saludar.html")

def saludar_a(request, nombre):
    return render(request, "app_proyecto/saludar_a.html", {'nombre': nombre})

def sumar(request, a, b):
    return render(request, "app_proyecto/sumar.html", 
    {'a': a,
    'b': b,
    'resulado': a + b
    }
    )

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "app_proyecto/familiares.html", 
  {"lista_familiares": lista_familiares})

def buscar(request):
    lista_de_nombres = ['German', 'Jorge', 'Mercedes'] 
    query = request.GET['q']
    if query in lista_de_nombres:
        indice_de_resultado = lista_de_nombres.index(query)
        resultado = lista_de_nombres[indice_de_resultado]
    else:
        resultado = 'no esta registrado' 
    return render(request, 'app_proyecto/buscar.html', {"resultado": resultado})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'app_proyecto/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form,'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})