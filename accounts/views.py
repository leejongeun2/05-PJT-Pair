from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationform
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


# Create your views here.

def index(request):
    users = get_user_model().objects.all()
    context = {
        "users":users
    }
    return render(request, "accounts/index.html", context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationform(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('reviews:index')
    else:
        form = CustomUserCreationform()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'reviews:index') 
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)



def logout(requst):
    pass

def detail(request):
    pass

def update(request):
    pass

def change_password(request):
    pass

def follow(request):
    pass
