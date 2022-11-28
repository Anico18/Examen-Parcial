from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import usuariosDjango
from django.urls import reverse

# Create your views here.

datos = usuariosDjango.objects.all().order_by('id')

def index(request):
   return render(request, 'gestion_tareas/index.html')

def dashboard(request):
    usuariosInfo = usuariosDjango.objects.all().order_by('id')
    if request.method == 'POST':
        if 'guardar' in request.POST:
            nuevo = []
            id = request.POST.get('idUsuario')
            nombre = request.POST.get('nombreUsuario')
            apellido = request.POST.get('apellidoUsuario')
            tarea = request.POST.get('tareaUsuario')
            fecha = request.POST.get('fechaUsuario')
            nuevo.append(str(id))
            nuevo.append(str(nombre))
            nuevo.append(str(apellido))
            nuevo.append(str(tarea))
            nuevo.append(str(fecha))
            usuariosDjango(id=str(id),nombre=str(nombre),apellido=str(apellido),
            tarea=str(tarea),fecha=str(fecha)).save()
            usuariosInfo = usuariosDjango.objects.all().order_by('id')
    elif 'filtrar' in request.POST:
        personafil = request.POST.get('persona')
        usuariosInfo = usuariosDjango.objects.filter(id=personafil)

    return render(request, 'gestion_tareas/dashboard.html',{
        'usuarios' : usuariosInfo,
    })

def new(request):
   return render(request, 'gestion_tareas/new.html')

def delete(request, id):
    usuario = usuariosDjango.objects.get(id=id)
    usuario.delete()
    return render(request, 'gestion_tareas/dashboard.html'),{
        'usuarios' : usuariosDjango.objects.all(),
    }

def info(request, id):
    usuario = usuariosDjango.objects.get(id=id)
    id = request.POST.get('idUsuario')
    nombre = request.POST.get('nombreUsuario')
    apellido = request.POST.get('apellidoUsuario')
    tarea = request.POST.get('tareaUsuario')
    fecha = request.POST.get('fechaUsuario')
    return render(request, 'gestion_tareas/info.html')