from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.



class Convention(models.Model):
    date_add = models.DateTimeField( auto_now=False, auto_now_add=True)
    date_update = models.DateTimeField( auto_now=True, auto_now_add=False)
    publish = models.BooleanField(default=False)

    class Meta:
        abstract = True

class TypeActeur(Convention):
    code_type_acteur = models.CharField(max_length=150)
    nom_type_acteur = models.CharField(max_length=250, default="agriculteur")
    libele = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom_type_acteur


class Acteur(Convention):
    type_acteur = models.ManyToManyField("web.TypeActeur",)
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



class TypeFilier(Convention):
    code_type_filiere = models.CharField(max_length=50)
    nom_type_filiere = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nom_type_filiere


class Filiere(Convention):
    code_filiere = models.CharField(max_length=50)
    nom_filiere = models.CharField(max_length=50)
    code_type_filiere = models.ForeignKey(TypeFilier, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nom_filiere
    
    def code_type_filieres(self):
        return self.code_type_filiere.code_type_filiere


class Region(Convention):
    nom_region = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom_region


class Localite(Convention):
    nom_localite = models.CharField(max_length=50)
    region = models.ForeignKey("web.Region", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nom_localite 



class Forme(Convention):
    nom_forme = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom_forme


class Maillon(Convention):
    nom_maillon = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_maillon

class Produit(Convention):
    maillon_produit = models.ManyToManyField(Maillon)
    nom_produit = models.CharField(max_length=250)
    code_produit = models.CharField(max_length=50)
    forme_produit = models.ForeignKey("web.Forme", on_delete=models.SET_NULL, null=True)
    code_filier = models.ForeignKey('web.Filiere', on_delete=models.SET_NULL, null=True)
    photo = models.FileField(upload_to='img_produit')
    description = models.TextField()
    
    
    def __str__(self):
        return self.nom_produit

    @property
    def code_filiere(self):
        return self.code_filier.code_filiere

class TypeMarche(Convention):
    code_type_marche = models.CharField(max_length=50)
    nom_type_marche = models.CharField(max_length=250)
    
    def __str__(self):
        return self.code_type_marche
    
class Marche(Convention):
    nom_marche = models.CharField(max_length=250, default="marché mamiAdjoua")
    code_marche = models.CharField(max_length=50)
    code_type_marche = models.ForeignKey("web.TypeMarche", on_delete=models.SET_NULL, null=True)
    locaclite = models.ForeignKey("web.Localite", on_delete=models.SET_NULL, null=True)
    jour_marche = models.ManyToManyField("app.Jour")
    code_superviseur =  models.ForeignKey(get_user_model(),on_delete=models.SET_NULL, null=True)
    coordonnee_geo = models.CharField(max_length=250)
    superficie = models.CharField( max_length=250)
    caracteristique = models.CharField( max_length=250)
    photo = models.FileField(upload_to='img_marche')
    
    def __str__(self):
        return self.nom_marche
    

class Magasin(Convention):
    code_magasin = models.CharField( max_length=50)
    code_acteur = models.ForeignKey("web.Acteur", on_delete=models.SET_NULL, null=True)
    localite_magasin = models.ForeignKey("web.Localite", on_delete=models.SET_NULL, null=True)
    coordonnee_geo = models.CharField(max_length=250)
    volume = models.IntegerField()
    caracteristique = models.TextField()
    photo = models.FileField(upload_to='img_magasin')
    
    def __str__(self):
        return self.code_magasin


CHOICE_SEX = (
    ("M","Homme"),
    ("F","Femme"),
)


class Enqueteur(Convention):
    code_enqueteur = models.CharField(max_length=50)
    nom_enqueteur = models.CharField(max_length=250)
    code_acteur = models.OneToOneField("users.User", on_delete=models.SET_NULL, null=True)
    localite_enqueteur = models.CharField(max_length=250)
    sexe = models.CharField(max_length=50, choices=CHOICE_SEX)
    photo = models.FileField(upload_to='img_enqueteur')
    
    def __str__(self):
        return self.nom_enqueteur
    
    def nomEnqueteur(self):
        return self.code_acteur.username
    


class Stock(Convention):
    code_stock = models.CharField( max_length=50)
    date_recolte = models.DateField(auto_now=True, auto_now_add=False)
    code_produit = models.ForeignKey("web.Produit", on_delete=models.SET_NULL, null=True)
    code_magasin = models.ForeignKey("web.Magasin", on_delete=models.SET_NULL, null=True)
    code_acteur = models.ForeignKey("web.Acteur", on_delete=models.SET_NULL, null=True)
    code_unite_produit = models.ForeignKey("app.UniteProduit", on_delete=models.SET_NULL, null=True)
    code_enqueteur = models.ForeignKey("web.Enqueteur", on_delete=models.SET_NULL, null=True)
    date_prelevement = models.DateField(auto_now=True, auto_now_add=False)
    quantite_stock = models.IntegerField()
    information_production = models.TextField()
    information_stockage = models.TextField()
    photo = models.FileField(upload_to='img_stock')
    
    def __str__(self):
        return self.code_stock
    
    def code_enqueteurs(self):
        return self.code_enqueteur.code_enqueteur
    

class SortieStock(Convention):
    date_sortie = models.DateTimeField(auto_now=True, auto_now_add=False)
    quantite_sortie = models.IntegerField()
    prix_vente = models.FloatField()
    code_acteur_destinateur = models.ForeignKey("web.Acteur", on_delete=models.SET_NULL, null=True)
    code_stock = models.ForeignKey("web.Stock", on_delete=models.CASCADE)
    code_enqueteur = models.ForeignKey("web.Enqueteur", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.code_stock.code_stock