from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def login(request):
  userName = request.POST.get('user_name')
  password = request.POST.get('password')
  
  user = authenticate(username=userName, password=password)
  
  if user is not None:
    return JsonResponse({"results": True})
  else:
    return JsonResponse({"results": False})



def signup(request):
  userName = request.POST.get('user_name')
  userEmail = request.POST.get('email')
  password = request.POST.get('password')

  user = User.objects.create_user(userName, userEmail, password)
  user.save()

  return JsonResponse({"results": True})
  
