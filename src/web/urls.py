from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name='home'),
    
    path('utilisateur', dashboard, name='utilisateur'),
    
    #path('register', singUp, name='register'),
]
