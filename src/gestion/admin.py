from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('code_commande', 'quantite_demande', 'quantite_livre', 'date_livraison', 'publish')
 

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'code_stock', 'code_enqueteurs', 'publish')
    
    def image_view(self, obj):
        return mark_safe(f'<img src= "{obj.photo.url}" style ="height:100px; width:200px>"')
 
 
@admin.register(SortieStock)
class SortieStockAdmin(admin.ModelAdmin):
    list_display = ('code_stock','publish')
    