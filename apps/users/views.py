from django.shortcuts import render, redirect
from .models import Users
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        password = request.POST["password"]


        user = Users.objects.create_user(email=email, phone_number=phone_number, password=password)

        user.save()

        return redirect("login")
    else:
        return render(request, "auth/register")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email,password=password)

        auth.login(request, user)

        return redirect("dashboard")
    else:
        return render(request, "auth/login.html")