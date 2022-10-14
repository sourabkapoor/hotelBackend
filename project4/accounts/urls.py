from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginuser, name="login"),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('logout/', views.logoutUser, name="logout")
]