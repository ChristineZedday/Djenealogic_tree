from django.db import models
from polymorphic.models import PolymorphicModel

class Individu(PolymorphicModel):
    nom = models.fields.CharField(max_length=100)
    
    surnom = models.fields.CharField(max_length=25, blank= True, null=True)
    date_naissance = models.DateField(blank= True, null=True)
    pere = models.ForeignKey('self', blank= True, null=True, on_delete=models.SET_NULL, related_name = 'pere_de')
    mere = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name= 'mere_de')

    def __str__(self):

        return f'{self.nom}'
    
class Personne(Individu):
    nom_usage = models.fields.CharField(max_length=100, blank= True, null=True)
    prenoms = models.fields.CharField(max_length=100, null=False)
    prenom_usuel = models.fields.CharField(max_length=30, null=False)

    def __str__(self):

        return f'{self.nom} {self.prenom_usuel}'
    
class Race(models.Model):
    nom = models.fields.CharField(max_length=100, blank= True, null=True)
    def __str__(self):

        return f'{self.nom}'
    
class Cheval(Individu):
    affixe = models.fields.CharField(max_length=15, blank= True, null=True)
    affixe_avant = models.fields.BooleanField(blank= True, null = True)
    robe = models.fields.CharField(max_length=200, blank= True, null=True)
    race = models.ForeignKey(Race, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        chaine =  f'{self.affixe} {self.nom}' if self.affixe_avant else f'{self.nom} {self.affixe}' 

        return chaine
    


    