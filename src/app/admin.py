from django.contrib import admin

from .models import Jour
# Register your models here.

@admin.register(Jour)
class JourAdmin(admin.ModelAdmin):
    list_display = ('jour', 'publish')