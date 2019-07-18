from django.shortcuts import render
from django.http import HttpResponse
from pendientes.models import Tarea
from random import randint
# Create your views here.

def index(request):
    listita = Tarea.objects.all()
    persona = {
        "nombre":"pedro",
        "edad":"22",
        "hobbies": "tomar terere",
        "lista_tareas":listita,
        }

    # return HttpResponse(saludo) #retornamos el saludo
    return render(request,"inicio.html", persona) #retornamos el saludo


def tarea(request):
    return HttpResponse("hola soy la vista tarea")

#crear una vista respuestas que retorne un texto cuando en el navegador entremos http___-___--/info
#lista crear la funcion /vista en viws y conectar a url usando path
def pepe(request):
    return HttpResponse("hola soy pepito")
def nuevo(request):
    return render(request, "inicio.html")
