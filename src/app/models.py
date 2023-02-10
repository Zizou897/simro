from django.db import models

# Create your models here.
from web.models import Convention

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
    
    