from django.contrib import admin
from  django.utils.safestring import mark_safe 
from .models import *
# Register your models here.

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'code_produit', 'code_filiere', 'nom_produit', 'publish')

    def image_view(self, obj):
        return mark_safe(f'<img src= "{obj.photo.url}" style ="height:100px; width:200px>"')
    

@admin.register(Unite)
class UniteAdmin(admin.ModelAdmin):
    list_display = ('code_unite', 'nom_unite', 'publish')
    

@admin.register(UniteProduit)
class UniteProduitAdmin(admin.ModelAdmin):
    list_display = ('code_unite_produit', 'code_unites', 'code_produits', 'publish')
 
 
@admin.register(Intrant)
class IntrantAdmin(admin.ModelAdmin):
    list_display = ('code_intrant', 'nom_intrant', 'quantite_utilise', 'code_superficies', 'publish')
 
 
@admin.register(TypeFilier)
class TypeFilierAdmin(admin.ModelAdmin):
    list_display = ('code_type_filiere', 'nom_type_filiere', 'publish')

    
@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ('code_filiere', 'nom_filiere', 'code_type_filieres', 'publish')


@admin.register(Forme)
class FormeAdmin(admin.ModelAdmin):
    list_display = ('nom_forme', 'publish')
