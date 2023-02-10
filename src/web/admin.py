from django.contrib import admin
from  django.utils.safestring import mark_safe 

from .models import *
# Register your models here.


@admin.register(TypeActeur)
class TypeActeurAdmin(admin.ModelAdmin):
    list_display = ('code_type_acteur', 'libele', 'publish')
    

@admin.register(Acteur)
class ActeurAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'code_acteur', 'publish')
    
    def image_view(self, obj):
        return mark_safe(f'<img src= "{obj.picture.url}" style ="height:100px; width:200px>"')

    
@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ('code_filiere', 'nom_filiere', 'publish')


@admin.register(TypeMarche)
class TypeMarcheAdmin(admin.ModelAdmin):
    list_display = ('code_type_marche', 'nom_type_marche', 'publish')
    
    
@admin.register(Marche)
class MarcheAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'code_marche', 'code_type_marche', 'locaclite', 'publish')

    def image_view(self, obj):
        return mark_safe(f'<img src= "{obj.photo.url}" style ="height:100px; width:200px>"')
    

@admin.register(Magasin)
class MagasinAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'code_magasin', 'localite_magasin', 'volume', 'publish')

    def image_view(self, obj):
        return mark_safe(f'<img src= "{obj.photo.url}" style ="height:100px; width:200px>"')


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'code_produit', 'code_filiere', 'nom_produit', 'publish')

    def image_view(self, obj):
        return mark_safe(f'<img src= "{obj.photo.url}" style ="height:100px; width:200px>"')
    
    
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('nom_region', 'publish')


@admin.register(Localite)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('nom_localite', 'publish')


@admin.register(Forme)
class FormeAdmin(admin.ModelAdmin):
    list_display = ('nom_forme', 'publish')


@admin.register(Maillon)
class MaillonAdmin(admin.ModelAdmin):
    list_display = ('nom_maillon', 'publish')

