from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Jour)
class JourAdmin(admin.ModelAdmin):
    list_display = ('jour', 'publish')
    
    
@admin.register(Campagne)
class CampagneAdmin(admin.ModelAdmin):
    list_display = ('code_campagne', 'publish')
    

@admin.register(Unite)
class UniteAdmin(admin.ModelAdmin):
    list_display = ('code_unite', 'nom_unite', 'publish')
    

@admin.register(UniteProduit)
class UniteProduitAdmin(admin.ModelAdmin):
    list_display = ('code_unite_produit', 'code_unites', 'code_produits', 'publish')
 
 
@admin.register(Intrant)
class IntrantAdmin(admin.ModelAdmin):
    list_display = ('code_intrant', 'nom_intrant', 'quantite_utilise', 'code_superficies', 'publish')
 
 
@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('code_commande', 'quantite_demande', 'quantite_livre', 'date_livraison', 'publish')
 
 
@admin.register(Prix)
class PrixAdmin(admin.ModelAdmin):
    list_display = ('code_unite_produit', 'code_marches', 'prix_unitaire', 'date_prix', 'publish')
 