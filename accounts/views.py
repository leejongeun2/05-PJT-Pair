from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationform, ProfileForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

# Create your views here.

def main(request):
    users = get_user_model().objects.all()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'reviews:index') 
    else:
        form = AuthenticationForm()
    context = {
        "users":users,
        'form': form,
    }
    return render(request, "accounts/main.html", context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationform(request.POST)
        profile_ = Profile()
        if form.is_valid():
            user = form.save()
            profile_.user = user
            profile_.save()
            auth_login(request, user)
            return redirect('reviews:index')
    else:
        form = CustomUserCreationform()
  
    context = {
        'form': form,
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



def logout(request):
    auth_logout(request)
    return redirect('reviews:index')


def detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    context = {
        'user': user,
        'reviews': user.review_set.all(),
    }
    return render(request, 'accounts/detail.html', context)

def update(request, pk):
    user = get_user_model().objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

def change_password(request, pk):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:main")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("accounts:login")

def follow(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user == user:
        messages.warning(request, '스스로 팔로우 할 수 없습니다.')
        return redirect('accounts:detail', pk)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)

    return redirect('accounts:detail', pk)

@login_required
def profile(request):
    user_ = request.user
    profile_ = user_.profile_set.all()[0]
    print(profile_)
    context = {
        "profile": profile_,
        'reviews': request.user.review_set.all(),
    }
    return render(request, "accounts/profile.html", context)


@login_required
def profile_update(request):
    user_ = get_user_model().objects.get(pk=request.user.pk)
    current_user = user_.profile_set.all()[0]
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=current_user)
    context = {
        "profile_form": form,
    }
    return render(request, "accounts/profile_update.html", context)
    
        
