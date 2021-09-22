from django.contrib import admin
from django.urls import path ,include
from .views import * 

urlpatterns = [
    path('', showHomePage), # at root url i.e http://localhost:8000/ showHomePage Function will be fired
    path('', include('authentication.urls')), # show login / signup page
    path('settings/', showSettingPage), #show setting page
    path('upload/', showUploadPage), #show setting page
    path('explore/', showExplorePage), #show setting page


]
