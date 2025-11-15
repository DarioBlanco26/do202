from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def index(request): 
    return HttpResponse("Esta sera una pagina basica del blog.")
