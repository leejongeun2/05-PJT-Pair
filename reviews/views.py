import json
from django.shortcuts import render, redirect
from .forms import ReviewForm, CommentForm
from .models import Comment, Review
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {"reviews": reviews}
    return render(request, "reviews/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()
        context = {"review_form": review_form}
    return render(request, "reviews/create.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        "review": review,
        "comment_form": comment_form,
        "comments": review.comments.all(),
    }
    return render(request, "reviews/detail.html", context)


@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
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
        return JsonResponse(
            {
                "content": comment.content,
            }
        )


@login_required
def comment_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    comment = False
    return JsonResponse(
        {
            "content": comment,
        }
    )
