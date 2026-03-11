from django.contrib import admin

from djens.models import *

class PersonneAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..

    list_display = ('prenom_usuel', 'nom', 'nom_usage') # liste les champs que nous voulons sur l'affichage de la liste

class ChevalAdmin(admin.ModelAdmin):
    list_display = ('nom', 'affixe') # liste les champs que nous voulons 

class RaceAdmin(admin.ModelAdmin):
    list_display = [('nom')] # liste les champs que nous voulons 


admin.site.register(Personne, PersonneAdmin)
admin.site.register(Individu)
admin.site.register(Cheval, ChevalAdmin)
admin.site.register(Race, RaceAdmin)