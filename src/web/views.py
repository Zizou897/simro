from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="login")
def home(request):
    template_name = 'app/admin/pages/index.html'
    context={}
    return render(request, template_name, context)

@login_required(login_url="login")
def dashboard(request):
    template_name = 'app/admin/pages/dashboard.html'
    context={}
    return render(request, template_name, context)
