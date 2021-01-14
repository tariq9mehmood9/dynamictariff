from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_view(request):
    if (request.user.is_authenticated):
        return redirect('userApp:home')
    else:
        return render(request, 'baseApp/home.html')

def about_view(request):
    return render(request, 'baseApp/about.html')

def abstract_view(request):
    return render(request, 'baseApp/abstract.html')