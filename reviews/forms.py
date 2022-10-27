from django.forms import ModelForm
from .models import Review, Comment


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title','content','image']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
