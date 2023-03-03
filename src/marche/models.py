from django.db import models
from django.contrib.auth import get_user_model

from produit.models import Convention
# Create your models here.


class TypeMarche(Convention):
    code_type_marche = models.CharField(max_length=50)
    nom_type_marche = models.CharField(max_length=250)
    
    def __str__(self):
        return self.code_type_marche
    
class Marche(Convention):
    nom_marche = models.CharField(max_length=250, default="marché mamiAdjoua")
    code_marche = models.CharField(max_length=50)
    code_type_marche = models.ForeignKey("marche.TypeMarche", on_delete=models.SET_NULL, null=True)
    locaclite = models.ForeignKey("parametrage.Localite", on_delete=models.SET_NULL, null=True)
    jour_marche = models.ManyToManyField("parametrage.Jour")
    code_superviseur =  models.ForeignKey(get_user_model(),on_delete=models.SET_NULL, null=True)
    coordonnee_geo = models.CharField(max_length=250)
    superficie = models.CharField( max_length=250)
    caracteristique = models.CharField( max_length=250)
    photo = models.FileField(upload_to='img_marche')
    
    def __str__(self):
        return self.nom_marche


class Magasin(Convention):
    code_magasin = models.CharField( max_length=50)
    code_acteur = models.ForeignKey("users.Acteur", on_delete=models.SET_NULL, null=True)
    localite_magasin = models.ForeignKey("parametrage.Localite", on_delete=models.SET_NULL, null=True)
    coordonnee_geo = models.CharField(max_length=250)
    volume = models.IntegerField()
    caracteristique = models.TextField()
    photo = models.FileField(upload_to='img_magasin')
    
    def __str__(self):
        return self.code_magasin