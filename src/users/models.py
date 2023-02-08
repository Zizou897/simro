from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from web.models import Convention


class User(AbstractUser):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    


class TypeActeur(Convention):
    code_type_acteur = models.CharField(max_length = 150)
    libele = models.CharField(max_length=50)
    
    def __str__(self):
        return self.code_type_acteur


class Acteur(Convention):
    type_acteur = models.ManyToManyField("users.TypeActeur",)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    code_acteur = models.CharField(max_length=50)
    coordonnee = models.CharField(max_length=50)
    picture = models.FileField(upload_to="acteur_img")
    description = models.TextField()
    
    def __str__(self):
        return self.user.username
