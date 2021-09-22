from django.shortcuts import render

# Create your views here.

def showLoginPage(request):
    return render(request,'authentication/login/login.html')

def showSignUpPage(request):
    return render(request,'authentication/signup/signup.html')
