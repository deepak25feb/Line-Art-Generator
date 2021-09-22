from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.

def showHomePage(request):
    value = request.session.get("status")  # Checking User Status 1 -> Logged , None : Not Logged
    if value is None:
        return redirect('/login/')

    # profilePhoto = UserData.objects.get(username=request.session.get("username"))
    # context = {"username":request.session.get("username"),
    #             "emailid":request.session.get("emailid"),
    #             "profilephoto":profilePhoto.profileimage,
    #             }
    # return render(request,'homeapp/profilepage/profilepage.html',context)
    return render(request,'home/homepage/homepage.html')


def showSettingPage(request):
    value = request.session.get("status")  # Checking User Status 1 -> Logged , None : Not Logged
    if value is None:
        return redirect('/login/')
    userName = request.session["username"]
    userEmailId = request.session["emailid"]
    context = {
        "username":userName,
        "useremail":userEmailId
    }
    return render(request,'home/settingpage/settingpage.html',context) 




def showUploadPage(request):
    value = request.session.get("status")  # Checking User Status 1 -> Logged , None : Not Logged
    if value is None:
        return redirect('/login/')

    return render(request,'home/uploadpage/uploadpage.html')

def showExplorePage(request):
    value = request.session.get("status")  # Checking User Status 1 -> Logged , None : Not Logged
    if value is None:
        return redirect('/login/')

    return render(request,'home/explorepage/explorepage.html')
    