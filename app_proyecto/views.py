from django import views
from django.forms import Form
from django.shortcuts import render, get_object_or_404
from app_proyecto.models import Familiar
from app_proyecto.forms import  Buscar, FamiliarForm
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

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'app_proyecto/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'app_proyecto/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})
      
class BorrarFamiliar(View):
  template_name = 'app_proyecto/familiares.html'
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiares})