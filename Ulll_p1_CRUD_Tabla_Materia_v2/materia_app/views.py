from django.shortcuts import render,redirect
from .models import Materia
# Create your views here.


def inicio_vista(request):
    # obtener todos los registros de la tabla materia
    listadomaterias=Materia.objects.all()
    return render(request,"gestionarmaterias.html",{"lasmaterias":listadomaterias})


def registrarmateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["txtcreditos"]

    guardarmateria=Materia.objects.create(codigo=codigo,materia=nombre, creditos=creditos)
    return redirect("/")