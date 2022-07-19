from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method == "POST":

        user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])

        login(request, user)

        return HttpResponse("success")

    else:
        return render(request, "register.html")