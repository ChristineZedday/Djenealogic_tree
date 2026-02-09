from django.contrib import admin

from djens.models import *

class PersonneAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..

    list_display = ('prenom_usuel', 'nom', 'nom_usage') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Personne, PersonneAdmin)
admin.site.register(Individu)
admin.site.register(Union)