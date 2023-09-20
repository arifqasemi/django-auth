from django.urls import path
from . import views
from django.contrib.auth import views as authentication_view
from .views import HomeView

urlpatterns = [
    path('home',views.HomeView.as_view(), name='home'),  # Change the path to an empty string
    # path('home', HomeView.as_view(), name='home'), 
    path('login', views.LoginView, name='login'),
    path('logout/', authentication_view.LogoutView.as_view(), name='logout'), 
    path('register', views.RegisterView.as_view(), name='register'),
    path('profile', views.ProfileView.as_view(), name='profile'),

]
