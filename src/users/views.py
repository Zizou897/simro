from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from django.contrib import messages

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
# Create your views here.

from users.models import User



def verify_email(email):
    try:
        validate_email(email)
        return False
    except ValidationError:
        return True


def singUp(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        address = request.POST.get('address')
        password = request.POST.get('Password')
        password1 = request.POST.get('Password1')
        
        if not username or username.isspace() or not email or email.isspace() or not phone or phone.isspace() or not address or address.isspace() or not password or password.isspace():
            messages.error(request, 'Veuillez remplir tous champs !!!')
            return redirect("register")
        
        if User.objects.filter(username=username):
            messages.error(request, 'username existant')
            return redirect("register")
        if verify_email(email):
            messages.error(request,'email incorrect')
            return redirect('register')
        print("######1######")
        
        if password != password1:
            messages.error(request,'les deux mots de passes doivent etre identique')
            print("######2######")
            return redirect('register')
        else:
            print("######3######")
            user = User.objects.create_user(username=username, email=email, phone=phone, address=address, password=password)
            user.is_active = False
            user.save()
            print(password)
            return redirect("login")
    
    template_name = 'admin/app/auth/register.html'
    context={}
    return render(request, template_name, context)



def singIn(request):
    if  request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or username.isspace()  or not password or password.isspace():
            messages.error(request, "Veuillez remplir tous les champs")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect("home")
        return redirect("login")
    """ 
    if  request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("******")
        if not username or username.isspace()  or not password or password.isspace():
            print("******12*****")
            messages.error(request, "Veuillez remplir tous les champs")
            return redirect("login")
        print("######1######")
        username_exists = User.objects.filter(username=username)
        if not username_exists:
            messages.error(request, "Nom d'utlisateur ou mot de passe incorrect")
            print("######2######")
            return redirect('login')
        user = User.objects.get(username=username)
        if user.is_active:
            my_user = authenticate(request,username=username, password=password)
            print("######3######")
            #print(user.username)
            print(my_user)
            if  my_user is not None:
                print("######4######")
                login(request, my_user)
                print(username)
                return redirect("home")
        messages.error(request,'Votre compte n\'est pas activé')
        return redirect('login')
    """
    template_name = 'app/admin/auth/login.html'
    context={}
    return render(request, template_name, context)


@login_required(login_url="login")
def signOut(request):
    logout(request)
    return redirect("login")
