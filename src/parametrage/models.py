from django.db import models

from produit.models import Convention
# Create your models here.

CHOICE_JOURS = (
    ("Lundi","Lundi"),
    ("Mardi","Mardi"),
    ("Mercredi","Mercredi"),
    ("Jeudi","Jeudi"),
    ("Vendredi","Vendredi"),
    ("Samedi","Samedi"),
    ("Dimanche","Dimanche"),
)

class Jour(Convention):
    jour = models.CharField(max_length=10, choices=CHOICE_JOURS)
    
    def __str__(self):
        return self.jour


class Region(Convention):
    nom_region = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom_region


class Localite(Convention):
    nom_localite = models.CharField(max_length=50)
    region = models.ForeignKey("parametrage.Region", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nom_localite 

class Campagne(Convention):
    code_campagne = models.CharField(max_length=50)
    libelle_campagne = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.code_campagne


class Maillon(Convention):
    nom_maillon = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_maillon
