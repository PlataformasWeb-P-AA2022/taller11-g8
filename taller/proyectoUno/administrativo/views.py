from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py
from administrativo.forms import *

# Create your views here.

def index(request):
 
    edificios = Edificio.objects.all()
  
    informacion_template = {'edificios': edificios, 'numero_edificios': len(edificios)}
    return render(request, 'index.html', informacion_template)


def obtener_edificio(request, id):

    edificio = Edificio.objects.get(pk=id)

    informacion_template = {'Edificio': Edificio}
    return render(request, 'obtener_Edificio.html', informacion_template)


def crear_Edificio(request):
    """
    """
    if request.method=='POST':
        formulario = EdificioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = EdificioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearEdificio_3.html', diccionario)


def editar_Edificio(request, id):
    """
    """
    Edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=Edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=Edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEdificio.html', diccionario)


def eliminar_Edificio(request, id):
    """
    """
    Edificio = Edificio.objects.get(pk=id)
    Edificio.delete()
    return redirect(index)


def crear_numero_telefonico(request):
    """
    """

    if request.method=='POST':
        formulario = NumeroTelefonicoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = NumeroTelefonicoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearNumeroTelefonico.html', diccionario)


def editar_numero_telefonico(request, id):
    """
    """
    telefono = NumeroTelefonico.objects.get(pk=id)
    if request.method=='POST':
        formulario = NumeroTelefonicoForm(request.POST, instance=telefono)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = NumeroTelefonicoForm(instance=telefono)
    diccionario = {'formulario': formulario}

    return render(request, 'crearNumeroTelefonico.html', diccionario)

def crear_numero_telefonico_Edificio(request, id):
    """
    """
    Edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = NumeroTelefonicoEdificioForm(Edificio, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = NumeroTelefonicoEdificioForm(Edificio)
    diccionario = {'formulario': formulario, 'Edificio': Edificio}

    return render(request, 'crearNumeroTelefonicoEdificio.html', diccionario)
