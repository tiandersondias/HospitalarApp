from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Aqui é o index<h1>")
    return render(request, 'hospitais/index.html')

def hospital(request):
    return HttpResponse("<h1>Aqui é a área de Hospital<h1>")
