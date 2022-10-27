from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model 

class CustomUserCreationform(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ("username", "email",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)