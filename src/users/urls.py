from django.urls import path
from django.contrib.auth import views as auth_views

from  .api_views import sign_out, SignUpView, LoginView
from .views import singIn, singUp, signOut

urlpatterns = [
    # site link
    path('login', singIn, name='login'),
    path('register', singUp, name='register'),
    path('logout', signOut, name='logout'),
    
    # Api link
    path('api/register/', SignUpView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='signin'),
    path('api/logout/', sign_out, name='signout'),

]
