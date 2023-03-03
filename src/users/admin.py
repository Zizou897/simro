from django.contrib import admin
from  django.utils.safestring import mark_safe 
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail

from .models import User, TypeActeur, Acteur

def send_email(admin_email, user_email, username, password):
    subject = "Création de compte"
    message = f"Votre compte vient d'etre créer. Voici vos access \nUsername: {username} \nPassword: {password} "
    from_email = admin_email
    to_email = user_email
    
    send_mail(subject, message, from_email, to_email, fail_silently=False)


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone','is_active')
    
    
    def save_model(self, request, obj, form, change):
        
        
        # do something with the obj before saving it
        print("cooool")
        try:
            username = User.objects.get(username=obj.username)
        except:
            obj.user = request.user
            send_email(obj.user.email, [obj.email], obj.username, obj.password)
            obj.password = make_password(obj.password)
        obj.save()

    #pbkdf2_sha256$390000$3aVRWjxx9XtGd5lADWeMBG$FXpLyu6JW05h282Y93vDswdqFrXJwz50N+S6fk5/P7w=
    

@admin.register(TypeActeur)
class TypeActeurAdmin(admin.ModelAdmin):
    list_display = ('code_type_acteur', 'libele', 'publish')
    

@admin.register(Acteur)
class ActeurAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'code_acteur', 'publish')
    
    def image_view(self, obj):
        return mark_safe(f'<img src= "{obj.picture.url}" style ="height:100px; width:200px>"')

