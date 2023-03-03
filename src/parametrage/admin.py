from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('nom_region', 'publish')


@admin.register(Localite)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('nom_localite', 'publish')


@admin.register(Maillon)
class MaillonAdmin(admin.ModelAdmin):
    list_display = ('nom_maillon', 'publish')

