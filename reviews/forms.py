from django.forms import ModelForm
from .models import Review

class ReviewForm(ModelForm):
    
   class Meta :
       Model = Review
       field = '__all__' 