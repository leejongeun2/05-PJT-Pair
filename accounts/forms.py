from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model 
from .models import Profile
from django import forms

class CustomUserCreationform(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ("username", "email",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]