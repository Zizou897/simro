from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from produit.models import Convention

class User(AbstractUser):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    acteur = models.ForeignKey("users.Acteur", on_delete=models.SET_NULL, null=True, blank=True)

class TypeActeur(Convention):
    code_type_acteur = models.CharField(max_length=150)
    nom_type_acteur = models.CharField(max_length=250, default="agriculteur")
    libele = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom_type_acteur


class Acteur(Convention):
    type_acteur = models.ManyToManyField("users.TypeActeur",)
    code_acteur = models.CharField(max_length=50)
    nom = models.CharField(max_length=250,  null=True, blank=True)
    coordonnee = models.CharField(max_length=250,  null=True, blank=True)
    categorie = models.CharField(max_length=250,  null=True, blank=True)
    picture = models.FileField(upload_to="acteur_img")
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    utilisateur = models.ForeignKey("users.User", related_name="user_acteur", on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nom

CHOICE_SEX = (
    ("M","Homme"),
    ("F","Femme"),
)


class Enqueteur(Convention):
    code_enqueteur = models.CharField(max_length=50)
    nom_enqueteur = models.CharField(max_length=250)
    code_acteur = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    localite_enqueteur = models.CharField(max_length=250)
    sexe = models.CharField(max_length=50, choices=CHOICE_SEX)
    photo = models.FileField(upload_to='img_enqueteur')
    
    def __str__(self):
        return self.nom_enqueteur
    
    def nomEnqueteur(self):
        return self.code_acteur.username
    