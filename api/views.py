from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import *
from django.shortcuts import redirect, render
import cv2
from django.core.files.base import ContentFile

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


@api_view(['POST'])
def resetUser(request):
    payload = [{"resetsuccess":False}]
    logoutStatus = request.data['logged']  # if True user was logged in else Guest User fired Reset Password
    if logoutStatus:
        request.session.flush()
        payload[0]["resetsuccess"] = True
    
        
    print(payload,"****Reset******")
    return Response(payload)




@api_view(['POST'])
def resetGuestUser(request):
    payload = [{"error":True,"email_status":False,"c_password_status":False,"n_password_status":False}]
    emailid = request.data['emailid']
    c_password = request.data['c_password']
    n_password = request.data['n_password']
    user = User.objects.filter(emailid=emailid).first() 
    if user is not None:    #Email id is correct
        payload[0]["email_status"] = True
        if user.password == c_password:
            payload[0]["c_password_status"] = True
            User.objects.filter(emailid=emailid).update(password=n_password)
            payload[0]["n_password_status"] = True
            payload[0]["error"] = False


    return Response(payload)


@api_view(['POST'])
def uploadUserImage(request):
    value = request.session.get("status")  # Checking User Status 1 -> Logged , None : Not Logged
    if value is None:
        return redirect('../login/')
    
    user = User.objects.get(username=request.session.get("username"))
    print("------->"+str(request.POST)+str(request.FILES))
    photoRef = Photos.objects.create(username=user,image=request.FILES.get('image'))
    ##############################################
    print("---->>>",photoRef,"------------",photoRef.image.path)
    convertedImage = converToLineArt(photoRef.image.path) # Converting Line Art Image
    binarFormatImage = cv2.imencode('.jpg', convertedImage)[1].tostring()
    file = ContentFile(binarFormatImage)
    print("...2..",ContentFile)
    Inst = ConvertedPhotos.objects.create(photooriginal=photoRef)
    Inst.imageconverted.save('translated.jpg', file, save=True)
    print("DONE--------------------")
    return redirect('../../') #This should redirect to Conversion Page [Art Line Conversion]
    
  
def converToLineArt(image):
    
    image_data = cv2.imread(image)
   
    gray_image = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
  
    inverted_image = 255 - gray_image

    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
 
    inverted_blurred = 255 - blurred
  
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
 
    return pencil_sketch


