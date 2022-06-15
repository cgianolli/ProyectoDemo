from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.template import loader
# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada=16740)
    curso.save()
    documento = f"Curso:{curso.nombre} Camada:{curso.camada}"
    return HttpResponse(documento)

def profesores(self):
    documento = f"Pagina de Profesores"
    return HttpResponse(documento)

def mi_plantilla(self):
    plantilla = loader.get_template('plantilla.html')
    documento = plantilla.render()
    return HttpResponse(documento)