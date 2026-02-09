from django.shortcuts import render
from django.http import HttpResponse
from djens.models import Personne


# Create your views here.

def home(request):
    return render(request, 'djens/home.html')

def personne(request,personne_id):
    personne = Personne.objects.get(id=personne_id)
    return render(request, 'djens/personne.html', {'personne': personne})

def personnes(request):
    personnes = Personne.objects.all()
    return render(request, 'djens/personnes.html', {'personnes' : personnes})
