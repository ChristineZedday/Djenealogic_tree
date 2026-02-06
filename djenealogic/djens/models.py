from django.db import models

class Individu(models.Model):
    nom = models.fields.CharField(max_length=100)
    
    surnom = models.fields.CharField(max_length=25, blank= True, null=True)
    date_naissance = models.DateField(blank= True, null=True)

class Personne(Individu):
    nom_usage = models.fields.CharField(max_length=100, blank= True, null=True)
    prenoms = models.fields.CharField(max_length=100, null=False)
    prenom_usuel = models.fields.CharField(max_length=30, null=False)

    def __str__(self):

        return f'{self.nom} {self.prenom_usuel}'