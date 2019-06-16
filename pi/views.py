from django.shortcuts import render
from django.http import HttpResponse	#n
# Create your views here.

def index(request):
    return HttpResponse("Hola:(")
