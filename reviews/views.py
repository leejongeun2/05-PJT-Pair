from django.shortcuts import render, redirect
from .forms import ReviewForm
<<<<<<< HEAD
from .models import Review
# Create your views here.

def index(request): 
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews' : reviews
    }
    return render(request, 'reviews/index.html', context)
=======

# Create your views here.

>>>>>>> 065cc126da8231786545cfe7d354fc0c1ddea42d

def index(request):

    return render(request, "reviews/index.html")


def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()
<<<<<<< HEAD
        context = {
            'review_form' : review_form
        }
    return render(request, 'reviews/create.html',context)


def detail(request,pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review' : review
    }
    return render(request, 'reviews/detail.html', context)
=======
    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/create.html", context)
>>>>>>> 065cc126da8231786545cfe7d354fc0c1ddea42d
