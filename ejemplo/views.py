from django.shortcuts import render
from ejemplo.models import Familiar

# Create your views here.
def index(request):
    return render(request, "ejemplo/saludar.html", {"nombre": "Wendy", 
        "apellido":"Manzanero"})

def index_dos(request, nombre, apellido):
        return render(request, "ejemplo/saludar.html", {"nombre": nombre, 
        "apellido": apellido,})

def index_tres(request):

    return render(request, "ejemplo/saludar.html", {"notas": [1,2,3,4,5,6,7,8]}) 

def imc(request, peso, altura):
    imc =  peso // altura    
    return render(request, "ejemplo/imc.html", {"imc": imc})

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})


