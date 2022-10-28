import json
from django.shortcuts import render, redirect
from .forms import ReviewForm, CommentForm
from .models import Comment, Review
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {
        "reviews": reviews,
        'profile': request.user.profile_set.all()[0]
    }
    return render(request, "reviews/index.html", context)

@login_required
def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit= False)
            review.user = request.user
            review.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()
        context = {
            "review_form": review_form,
            'profile': request.user.profile_set.all()[0],
            }
    return render(request, "reviews/create.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        "review": review,
        "comment_form": comment_form,
        "comments": review.comments.all(),
        'profile': request.user.profile_set.all()[0],
    }
    return render(request, "reviews/detail.html", context)

@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review )
        if form.is_valid():
            form.save()
            return redirect("reviews:detail", review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(
        request,
        "reviews/update.html",
        {
            "form": form,
        },
    )


@login_required
def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("reviews:index")


@login_required
def comment_create(request, pk):
    review = Review.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.save()
    return redirect('reviews:detail', pk)

@login_required
def comment_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', review_pk)

@login_required
def like(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
        is_liked = False
    else:
        review.like_users.add(request.user)
        is_liked = True
    context = {'isLiked': is_liked, 'likeCount': review.like_users.count()}
    return JsonResponse(context)

@property
def image_url(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image.url