from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Account

def index(request):
  if request.user.is_authenticated:
    return redirect("home")
  return redirect("login")

def loginuser(request):
  if request.method == "POST":
    userEmail = request.POST.get('loginEmail')
    password = request.POST.get('loginPassword')

    user = authenticate(email=userEmail, password=password)

    if user is not None:
      login(request, user)
      return redirect("home")
    else:
      return JsonResponse({"results": False})
  
  if request.method == "GET":
    if request.user.is_authenticated:
      return redirect('home')
    return render(request, 'login.html')

def signup(request):
  if request.method == "POST":
    userName = request.POST.get('user_name')
    userEmail = request.POST.get('email')
    password = request.POST.get('password')

    user = Account.objects.create_user(userEmail, userName, password)
    user.save()

    return redirect('login')
  
  if request.method == "GET":
    if request.user.is_authenticated:
      return redirect('home')
    return render(request, "signup.html")

def home(request):
  if request.method == "GET":
    if request.user.is_authenticated:
      return render(request, 'home.html')
    else:
      return redirect('login')

def logoutUser(request):
  if request.method == "GET":
    if request.user.is_authenticated:
      logout(request)
      return redirect('login')
  
