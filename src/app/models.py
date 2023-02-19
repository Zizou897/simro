from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from web.models import Convention, Produit, Acteur

User = get_user_model()

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
    

class Campagne(Convention):
    code_campagne = models.CharField(max_length=50)
    libelle_campagne = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.code_campagne
    
    
class Superficie(Convention):
    code_superficie = models.CharField(max_length=50)
    nom_superficie = models.CharField(max_length=250)
    code_acteur = models.ForeignKey("web.Acteur", on_delete=models.SET_NULL, null=True)
    code_campagne = models.ForeignKey("app.Campagne", on_delete=models.SET_NULL, null=True)
    code_produit = models.ForeignKey("web.Produit", on_delete=models.SET_NULL, null=True)
    localite = models.CharField(max_length=250)
    superfice_ha = models.FloatField()
    date_semi = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.code_superficie


class Unite(Convention):
    code_unite = models.CharField(max_length=50)
    nom_unite = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nom_unite

class UniteProduit(Convention):
    code_unite_produit = models.CharField(max_length=50)
    code_unite = models.ForeignKey("app.Unite", on_delete=models.SET_NULL, null=True)
    code_produit = models.ForeignKey("web.Produit", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.code_unite_produit
    
    @property
    def code_produits(self):
        return self.code_produit.code_produit
    
    @property
    def code_unites(self):
        return self.code_unite.code_unite


class Intrant(Convention):
    code_intrant = models.CharField(max_length=50)
    nom_intrant = models.CharField(max_length=50)
    code_superficie = models.ForeignKey('web.Filiere', on_delete=models.CASCADE)
    code_acteur_vendu = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    quantite_utilise = models.IntegerField(50)
    
    def __str__(self):
        return self.code_intrant
    
    def code_superficies(self):
        return self.code_superficie.code_superficie
    

class Commande(Convention):
    code_commande = models.CharField( max_length=50)
    date_commande = models.DateTimeField(auto_now=True, auto_now_add=False)
    code_acteur_acheteur = models.ForeignKey("web.Acteur", related_name='customer',on_delete=models.SET_NULL, null=True)
    code_acteur_vendeur = models.ForeignKey("web.Acteur", related_name='seller',on_delete=models.SET_NULL, null=True)
    quantite_demande = models.IntegerField()
    quantite_livre = models.IntegerField()
    date_livraison = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    
    def __str__(self):
        return self.code_commande


class Prix(Convention):
    code_enqueteur = models.ForeignKey("web.Enqueteur", on_delete=models.SET_NULL, null=True)
    code_unite_produit = models.ForeignKey("app.UniteProduit", on_delete=models.SET_NULL, null=True)
    code_marche = models.ForeignKey("web.Marche", on_delete=models.SET_NULL, null=True)
    prix_unitaire = models.FloatField()
    date_prix = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.prix_unitaire
    
    @property
    def code_marches(self):
        return self.code_marche.code_marche