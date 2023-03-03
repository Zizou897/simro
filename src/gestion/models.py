from django.db import models

from produit.models import Convention
# Create your models here.

class Commande(Convention):
    code_commande = models.CharField( max_length=50)
    date_commande = models.DateTimeField(auto_now=True, auto_now_add=False)
    code_acteur_acheteur = models.ForeignKey("users.Acteur", related_name='customer',on_delete=models.SET_NULL, null=True)
    code_acteur_vendeur = models.ForeignKey("users.Acteur", related_name='seller',on_delete=models.SET_NULL, null=True)
    quantite_demande = models.IntegerField()
    quantite_livre = models.IntegerField()
    date_livraison = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    
    def __str__(self):
        return self.code_commande



class Stock(Convention):
    code_stock = models.CharField( max_length=50)
    date_recolte = models.DateField(auto_now=True, auto_now_add=False)
    code_produit = models.ForeignKey("produit.Produit", on_delete=models.SET_NULL, null=True)
    code_magasin = models.ForeignKey("marche.Magasin", on_delete=models.SET_NULL, null=True)
    code_acteur = models.ForeignKey("users.Acteur", on_delete=models.SET_NULL, null=True)
    code_unite_produit = models.ForeignKey("produit.UniteProduit", on_delete=models.SET_NULL, null=True)
    code_enqueteur = models.ForeignKey("users.Enqueteur", on_delete=models.SET_NULL, null=True)
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
    code_acteur_destinateur = models.ForeignKey("users.Acteur", on_delete=models.SET_NULL, null=True)
    code_stock = models.ForeignKey("gestion.Stock", on_delete=models.CASCADE)
    code_enqueteur = models.ForeignKey("users.Enqueteur", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.code_stock.code_stock