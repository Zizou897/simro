from django.db import models


# Create your models here.


class Convention(models.Model):
    date_add = models.DateTimeField( auto_now=False, auto_now_add=True)
    date_update = models.DateTimeField( auto_now=True, auto_now_add=False)
    publish = models.BooleanField(default=False)

    class Meta:
        abstract = True




class TypeFilier(Convention):
    code_type_filiere = models.CharField(max_length=50)
    nom_type_filiere = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nom_type_filiere


class Filiere(Convention):
    code_filiere = models.CharField(max_length=50)
    nom_filiere = models.CharField(max_length=50)
    #code_type_filiere = models.ForeignKey(TypeFilier, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom_filiere

class Produit(Convention):
    nom_produit = models.CharField(max_length=250)
    code_produit = models.CharField(max_length=50)
    forme_produit = models.CharField(max_length=50)
    maillon_produit = models.CharField(max_length=50)
    code_filier = models.ForeignKey('web.Filiere',on_delete=models.CASCADE)
    photo = models.FileField(upload_to='img_produit')
    description = models.TextField()
    
    
    def __str__(self):
        return self.nom_produit


class TypeMarche(Convention):
    code_type_marche = models.CharField(max_length=50)
    nom_type_marche = models.CharField(max_length=250)
    
    def __str__(self):
        return self.code_type_marche
    
class Marche(Convention):
    code_marche = models.CharField(max_length=50)
    code_type_marche = models.ForeignKey("web.TypeMarche", on_delete=models.CASCADE)
    locaclite = models.CharField(max_length=250)
    jour_marche = models.CharField(max_length=50)
    code_superviseur =  models.CharField(max_length=50)
    coordonnee_geo = models.CharField(max_length=250)
    superficie = models.CharField( max_length=250)
    caracteristique = models.CharField( max_length=250)
    photo = models.FileField(upload_to='img_marche')
    
    def __str__(self):
        return self.code_marche
    

class Magasin(Convention):
    code_magasin = models.CharField( max_length=50)
    code_acteur = models.ForeignKey("users.Acteur", on_delete=models.CASCADE)
    localite_magasin = models.CharField(max_length=250)
    coordonnee_geo = models.CharField(max_length=250)
    volume = models.IntegerField()
    caracteristique = models.TextField()
    photo = models.FileField(upload_to='img_magasin')
    
    def __str__(self):
        return self.code_magasin