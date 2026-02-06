from django.shortcuts import render
from django.http import HttpResponse
from djens.models import Individu


# Create your views here.

def home(request):
    return render(request, 'djens/home.html')

def individu(request):
    return render(request, 'djens/individu.html')

def individus(request):
    individus = Individu.objects.all()
    return render(request, 'djens/individus.html', {'individus' : individus})
