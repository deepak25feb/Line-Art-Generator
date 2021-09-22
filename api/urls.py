from django.contrib import admin
from django.urls import path ,include
from .views import *

urlpatterns = [
    path('login/', loginUser),
    path('signup/', signUpUser),
    path('logout/', logoutUser),
    
]
