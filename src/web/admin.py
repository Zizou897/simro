from django.contrib import admin
from  django.utils.safestring import mark_safe 

from .models import *
# Register your models here.


    
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