from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Convention(models.Model):
    date_add = models.DateTimeField( auto_now=False, auto_now_add=True)
    date_update = models.DateTimeField( auto_now=True, auto_now_add=False)
    publish = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Produit(Convention):
    maillon_produit = models.ManyToManyField("parametrage.Maillon",)
    nom_produit = models.CharField(max_length=250)
    code_produit = models.CharField(max_length=50)
    forme_produit = models.ForeignKey("produit.Forme", on_delete=models.SET_NULL, null=True)
    code_filier = models.ForeignKey('produit.Filiere', on_delete=models.SET_NULL, null=True)
    photo = models.FileField(upload_to='img_produit')
    description = models.TextField()
    
    
    def __str__(self):
        return self.nom_produit

    @property
    def code_filiere(self):
        return self.code_filier.code_filiere
    

class TypeFilier(Convention):
    code_type_filiere = models.CharField(max_length=50)
    nom_type_filiere = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nom_type_filiere



class Filiere(Convention):
    code_filiere = models.CharField(max_length=50)
    nom_filiere = models.CharField(max_length=50)
    code_type_filiere = models.ForeignKey("produit.TypeFilier", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nom_filiere
    
    def code_type_filieres(self):
        return self.code_type_filiere.code_type_filiere
    

class Forme(Convention):
    nom_forme = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom_forme


class Intrant(Convention):
    code_intrant = models.CharField(max_length=50)
    nom_intrant = models.CharField(max_length=50)
    code_superficie = models.ForeignKey('produit.Filiere', on_delete=models.SET_NULL, null=True)
    #code_acteur_vendu = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    quantite_utilise = models.IntegerField(50)
    
    def __str__(self):
        return self.code_intrant
    
    def code_superficies(self):
        return self.code_superficie.code_superficie


class UniteProduit(Convention):
    code_unite_produit = models.CharField(max_length=50)
    code_unite = models.ForeignKey("produit.Unite", on_delete=models.SET_NULL, null=True)
    code_produit = models.ForeignKey("produit.Produit", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.code_unite_produit
    
    @property
    def code_produits(self):
        return self.code_produit.code_produit
    
    @property
    def code_unites(self):
        return self.code_unite.code_unite


class Unite(Convention):
    code_unite = models.CharField(max_length=50)
    nom_unite = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nom_unite