from django.urls import path
from . import views


app_name = "reviews"
urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),   
    path('<int:pk>/', views.detail, name = 'detail'),
]
=======
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
]
>>>>>>> 065cc126da8231786545cfe7d354fc0c1ddea42d
