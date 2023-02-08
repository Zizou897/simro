from django.contrib import admin
from  django.utils.safestring import mark_safe 

from .models import User, TypeActeur, Acteur
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone','is_active')
    
    

@admin.register(TypeActeur)
class TypeActeurAdmin(admin.ModelAdmin):
    list_display = ('code_type_acteur', 'libele', 'publish')
    

@admin.register(Acteur)
class ActeurAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'code_acteur',  'user', 'publish')
    
    def image_view(self, obj):
        return mark_safe(f'<img src= "{obj.picture.url}" style ="height:100px; width:200px>"')
    

