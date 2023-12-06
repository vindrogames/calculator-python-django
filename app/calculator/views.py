from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "calculator/index.html")

def suma(request):
    operando_uno = request.GET['op1']
    operando_dos = request.GET['op2']
    suma = int(operando_uno) + int(operando_dos)
    return HttpResponse(suma)

def resta(request):
    operando_uno = request.GET['op1']
    operando_dos = request.GET['op2']
    resta = int(operando_uno) - int(operando_dos)
    return HttpResponse(resta)

