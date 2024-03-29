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

def mult(request):
    operando_uno = request.GET['op1']
    operando_dos = request.GET['op2']
    mult = int(operando_uno) * int(operando_dos)
    return HttpResponse(mult)

def divide(request):
    operando_uno = request.GET['op1']
    operando_dos = request.GET['op2']
    div = int(operando_uno) / int(operando_dos)
    return HttpResponse(div)

def clicked(request):
    return HttpResponse("htmx works!")