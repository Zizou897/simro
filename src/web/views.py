from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="login")
def home(request):
    template_name = 'app/pages/index.html'
    context={}
    return render(request, template_name, context)
