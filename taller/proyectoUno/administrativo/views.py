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

    informacion_template = {'edificio': edificio}
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

    return render(request, 'crearEdificio.html', diccionario)


def editar_Edificio(request, id):
    """
    """
    Edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEdificio.html', diccionario)


def eliminar_Edificio(request, id):
    """
    """
    Edificio = Edificio.objects.get(pk=id)
    Edificio.delete()
    return redirect(index)


def crear_departamento(request):
    """
    """

    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = departamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearDepartamento.html', diccionario)


def editar_departamento(request, id):
    """
    """
    nombre_prop = departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=nombre_prop)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = departamentoForm(instance=nombre_prop)
    diccionario = {'formulario': formulario}

    return render(request, 'creardepartamento.html', diccionario)

def crear_departamento_edificio(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoEdificioForm(edificio, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoEdificioForm(edificio)
    diccionario = {'formulario': formulario, 'edificio': edificio}

    return render(request, 'crearDepartamentoEdificio.html', diccionario)
