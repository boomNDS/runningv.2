from pyrebase import pyrebase
from django.shortcuts import render,redirect
from django.contrib import auth
from backend import models

config = {
    "apiKey": "AIzaSyBSR_7iWZw3gOVC3x25O_n2yzhS-V3b22M",
    "authDomain": "runningthailand-dc7f9.firebaseapp.com",
    "databaseURL": "https://runningthailand-dc7f9.firebaseio.com",
    "projectId": "runningthailand-dc7f9",
    "storageBucket": "runningthailand-dc7f9.appspot.com",
    "messagingSenderId": "946973593994",
    "appId": "1:946973593994:web:5ac16fb323854776"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()
# Create your views here.

def regis(request):
    context = {
        'page_title': "รายการคำขอลางานของฉัน",
        'e': '',
    }
    return render(request, template_name='register/step1.html', context=context)

def index(request):

    context = {
        'page_title': "รายการคำขอลางานของฉัน",
        'e': request.session.get('my_email', ''),
    }
    return render(request, template_name='index.html', context=context)


def signin(request):

    context = {
        'page_title': "รายการคำขอลางานของฉัน",
    }
    return render(request, template_name='signin.html', context=context)

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    request.session['my_email'] = email
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request,"signin.html",{"msg":message})
    print(user['idToken'])
    return render(request, "index.html",{"e":request.session['my_email']})
    
def logout(request):
    auth.logout(request)
    return render(request,'signin.html')

def signup(request):

    context = {
        'page_title': "รายการคำขอลางานของฉัน",
    }
    return render(request, template_name='signup.html', context=context)

def postsignup(request):

    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
        uid = user['localId']
        data = {"fname": fname, "lname": lname}
        db.child("users").child(uid).child("details").set(data)
    except:
        message="Unable to create account try again"
        return render(request,"signup.html",{"messg":message})    
    return render(request,"signIn.html")

def editme(request):
    user = authe.current_user
    uid = user['localId']
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        newdata = {"fname": fname, "lname": lname}
        db.child("users").child(uid).child("details").update(newdata)
    data = db.child("users").child(uid).child("details").get()
    jsondata = data.val()
    context = {
        'e': request.session['my_email'],
        'uid': uid,
        'data': jsondata
    }
    return render(request, template_name='editme.html', context=context)

