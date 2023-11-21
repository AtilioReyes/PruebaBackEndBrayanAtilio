from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profesorJefe/index', views.index),
    path('profesorJefe/MostrarDatos',views.MostrarDatos),
    path('profesorJefe/Registrar',views.registrarProfJefe)
    
]
