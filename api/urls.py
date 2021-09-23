from django.contrib import admin
from django.urls import path ,include
from .views import *

urlpatterns = [
    path('login/', loginUser),
    path('signup/', signUpUser),
    path('logout/', logoutUser),
    path('resetpassword/', resetUser), # Make all User Guest
    path('resetGuestUser/', resetGuestUser), #All user end up Guest User
    
    
]
