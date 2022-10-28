from django import forms
from django.forms import ModelForm
from .models import Review, Comment
from django.forms import widgets


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title','content','image']


class CommentForm(ModelForm):
    content = forms.CharField(
        label='',
        widget=widgets.TextInput(
            attrs={
                'class': 'w-100',
                'placeholder': '댓글 작성',
            })
        )
    class Meta:
        model = Comment
        fields = ["content"]
        
        