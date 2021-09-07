from django.shortcuts import HttpResponse, redirect # agrega redirección a la declaración de importación
from django.http import JsonResponse

def root(request):
	return redirect("/blogs")

# def blog(request):
# 	return HttpResponse("<h1>esto es el blog</h1>")

def index(request):
	return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
	return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
	return redirect("/")

def show(request, number):
	return HttpResponse(f"placeholder para mostrar el blog número: {number}")

def edit(request, number):
	return HttpResponse(f"placeholder para editar el blog número: {number}")

def destroy(request,number):
	return redirect("/blogs")

def json(request):
    data = [{'name': 'Peter', 'email': 'peter@example.org'},
            {'name': 'Julia', 'email': 'julia@example.org'}]
    return JsonResponse(data, safe=False)