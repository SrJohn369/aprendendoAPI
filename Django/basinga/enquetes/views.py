from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Olá mundo. Estamos no index das enquetes.")

# tendeu?
