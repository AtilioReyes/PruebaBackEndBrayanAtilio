from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import FormProfeJefe

def index(request):
    return render(request,'ProfesorJefe/index.html')

def MostrarDatos(request):
    profesor = ProfJefe.objects.all()
    return render(request,'ProfesorJefe/Ver.html',{"profesor":profesor})

def registrarProfJefe (request):
    form = FormProfeJefe()
    if request.method == 'POST' :
        form = FormProfeJefe(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data ={'form' : form}
    return render(request,'ProfesorJefe/registrar.html',data)

def eliminarProfesor(request,id):
    form = ProfJefe.objects.get(id = id)
    form.delete()
    return redirect('ProfesorJefe/Ver.html')

def actualizarProfesor(request,id):
    profe = ProfJefe.objects.get(id = id)
    form = FormProfeJefe(instance=profe)
    if request.method == 'POST':
        form  = FormProfeJefe(request.POST, instance=profe)
        if form.is_valid():
            form.save()
        return index(request)
    data ={'form' : form}
    return render(request,'ProfesorJefe/registrar.html',data)

# Create your views here.
