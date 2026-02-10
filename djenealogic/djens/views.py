from django.shortcuts import render
from django.http import HttpResponse
from djens.models import Personne
from djens.forms import ContactUsForm
from django.core.mail import send_mail


# Create your views here.

def home(request):
    return render(request, 'djens/home.html')

def personne(request,personne_id):
    personne = Personne.objects.get(id=personne_id)
    return render(request, 'djens/personne.html', {'personne': personne})

def personnes(request):
    personnes = Personne.objects.all()
    return render(request, 'djens/personnes.html', {'personnes' : personnes})

def contact(request):
     

     if request.method == 'POST':

     # créer une instance de notre formulaire et le remplir avec les données POST

        form = ContactUsForm(request.POST)
        if form.is_valid():

            send_mail(

            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Djenealogic Contact Us form',

            message=form.cleaned_data['message'],

            from_email=form.cleaned_data['email'],

            recipient_list=['chrizedday@free.fr'],

        )

     else:

    # ceci doit être une requête GET, donc créer un formulaire vide

        form = ContactUsForm()
     return render(request,'djens/contact.html', {'form': form})  # passe ce formulaire au gabarit
 