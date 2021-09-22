from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import *

@api_view(['POST'])
def loginUser(request):
    payload = [{"userexist":False,"password":False}]
    userEmail = request.data['emailid']
    userPassword = request.data['password']
    user = User.objects.filter(emailid=userEmail).first() #if user not exits -> None
    if user is not None:
        payload[0]["userexist"] = True
        if user.password == userPassword:
            payload[0]["password"] = True
            request.session["status"] = 1 # Setting User Session
            request.session["username"] = user.username
            request.session["emailid"] = userEmail

    return Response(payload)



@api_view(['POST'])
def signUpUser(request):
    payload = [{"error":True,"username_status":"invalid","emailid_status":"invalid","password_status":"weak"}]
    userName = request.data['username']
    userEmail = request.data['emailid']
    userPassword = request.data['password']
    user = User.objects.filter(emailid=userEmail).first() #if user not exits -> None
    if user is None:
        payload[0]["emailid_status"] = "valid"
        payload[0]["password_status"] = "strong"   #validation defer <- will be done later
        username_check = User.objects.filter(username=userName).first() #if username isn't unique -> None
        if username_check is None:
            payload[0]["username_status"] = "valid"
            payload[0]["error"] = False
            User.objects.create(username=userName,emailid=userEmail,password=userPassword) # Saving User to Database
            request.session["status"] = 1 # Setting User Session
            request.session["username"] = userName
            request.session["emailid"] = userEmail
    print(payload,"**********")
    return Response(payload)
    



@api_view(['POST'])
def logoutUser(request):
    payload = [{"logout":False}]
    logoutStatus = request.data['logout']
    if logoutStatus:
        request.session.flush()
        payload[0]["logout"] = True
        
    print(payload,"**********")
    return Response(payload)