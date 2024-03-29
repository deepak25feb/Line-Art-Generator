from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from user.forms import *
# Create your views here.

def showHomePage(request):
    value = request.session.get("status")  # Checking User Status 1 -> Logged , None : Not Logged
    if value is None:
        return redirect('/login/')

    user = User.objects.get(username=request.session.get("username")) # Getting User name from session
    i =  Photos.objects.filter(username=user) #Getting All Images from that User
    profilePhoto = ProfilePhotos.objects.get(username=user)
    images = []
    for imag_e in i:
        images.append(imag_e.image)
        images.append(imag_e.imageconverted)

    context= {
        "username":user.username,
        "profilephoto":profilePhoto.profilephoto,
        "images":images
    }
    # profilePhoto = UserData.objects.get(username=request.session.get("username"))
    # context = {"username":request.session.get("username"),
    #             "emailid":request.session.get("emailid"),
    #             "profilephoto":profilePhoto.profileimage,
    #             }
    # return render(request,'homeapp/profilepage/profilepage.html',context)
    return render(request,'home/homepage/homepage.html',context)


def showSettingPage(request):
    value = request.session.get("status")  # Checking User Status 1 -> Logged , None : Not Logged
    if value is None:
        return redirect('/login/')
    
    Profileform = ProfilePhotosForm()
    userName = request.session["username"]
    userEmailId = request.session["emailid"]
    context = {
        "username":userName,
        "useremail":userEmailId,
        "form":Profileform
    }
    return render(request,'home/settingpage/settingpage.html',context) 




def showUploadPage(request):
    form = PhotosForm()
    context= {
        "form":form #This is only Contain ImageField [Check form.py in user app]
    }
    value = request.session.get("status")  # Checking User Status 1 -> Logged , None : Not Logged
    if value is None:
        return redirect('/login/')

    return render(request,'home/uploadpage/uploadpage.html',context)

def showExplorePage(request):
    value = request.session.get("status")  # Checking User Status 1 -> Logged , None : Not Logged
    if value is None:
        return redirect('/login/')
    
    # userName = request.session.get("username")
    # userData = User.objects.filter(username=userName).first()
    # userPhotos = Photos.objects.filter(username = userData).all()
    # print("HHHHHHHH->",userPhotos)
    # context = {"data":[]}
    # for imageObj in list(userPhotos):
    #     context["data"].append(imageObj.image)
    #     context["data"].append(imageObj.imageconverted)
    # print("HHHHHHHH----------------->",context)
    #00000000000000000000000000000000000000000000000000000000000000000000000000000000
    context = {"data":[]}
    userQuery = User.objects.all()
    for user in list(userQuery):
        userConvertedPhotos = Photos.objects.filter(username = user).all()
        for imageObj in list(userConvertedPhotos):
            context["data"].append((user.username,imageObj.imageconverted))

    print("HHHHHHHH----------------->",context)
    # print("----***",list(userAllOriginalPhotos))
    # obj = list(userAllOriginalPhotos)
    # aXX = ConvertedPhotos.objects.get(photooriginal = 31)
    # print("_____________",aXX)
    # request.session.flush();
    #print("RRRRRRRRRRRRRRRRRRR",ConvertedPhotos.objects.get(photooriginal=list(userAllOriginalPhotos)[0]))
    # context = []
    # for PhotosObj in list(userAllOriginalPhotos):
    # #     Photodx = Photos.objects.get(image=imageObj.image)
    #     userTranslatedPhoto = ConvertedPhotos.objects.get(photooriginal = PhotosObj)
    #     context.append((PhotosObj.image,userTranslatedPhoto.imageconverted))
    # print(context)

    return render(request,'home/explorepage/explorepage.html',context)
    