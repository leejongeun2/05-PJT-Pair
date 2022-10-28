from django.urls import path
from . import views
app_name= 'accounts'


urlpatterns = [
    path('', views.main, name = 'main'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/<int:pk>/', views.detail, name='detail'),
    path('accounts/update/', views.update, name='update'),
    path('accounts/password/', views.change_password, name='change_password'),
    path('accounts/<int:pk>/follow/', views.follow, name='follow'),
    path('accounts/delete/', views.delete, name='delete'),
    path("accounts/profile/", views.profile, name="profile"),
    path("accounts/profile/update/", views.profile_update, name="profile_update"),
    
]