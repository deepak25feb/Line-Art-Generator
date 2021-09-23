from django.contrib import admin
from django.urls import path ,include
from .views import * 

urlpatterns = [
   path('login/',showLoginPage),
   path('signup/',showSignUpPage),
   path('resetPassword/',showResetPasswordPage),
   
]
