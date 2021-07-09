
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
# Create your views here.
def root(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")
def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")
def create(request):
    return redirect('/')
def show(request, num):
    return HttpResponse(f"placeholder para mostrar el blog numero {num}")
def edit(request, num):
    return HttpResponse(f"placeholder para editar el blog {num}")
def destroy(request, num):
    return redirect("/")
def bonus(request):
    prueba= JsonResponse({'Titulo':'Las manzanas son rojas'})
    return HttpResponse(prueba)#prueba 1 
