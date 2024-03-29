from pyrebase import pyrebase
from django.shortcuts import render,redirect
from django.contrib import auth
from backend.models import *

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

def competition_result(request):

    context = {
        'e': request.session.get('my_email', ''),
        'competitions': CompetitionResultsInformation.objects.all(),
        # 'isregis': RegisterInfo.objects.filter(user_email=request.session.get('my_email', '')).exists()
    }
    return render(request, template_name='competitions.html', context=context)
def certificate(request):
    test = RegisterInfo.objects.get(user_email=request.session.get('my_email', ''))
    runner = Runner.objects.filter(regist_id=test)
    allimgs = []
    for i in runner:
        allimgs.append(Certificate.objects.get(runner_bib=i))
    context = {
        'e': request.session.get('my_email', ''),
        'test': test,
        'runner': runner,
        'allimgs': allimgs,
    }
    return render(request, template_name='certificate.html', context=context)

def live(request):
    live = Runner_Checkpoint.objects.all()
    context = {
        'e': request.session.get('my_email', ''),
        'live': live
    }
    return render(request, template_name='live.html', context=context)

def regis(request):
    context = {
        'e': request.session.get('my_email', ''),
    }
    return render(request, template_name='register/step1.html', context=context)

def index(request):
    new = News.objects.all()
    allteam = Team.objects.all()
    context = {
        'e': request.session.get('my_email', ''),
        'new': new,
        'allteam': allteam
    }
    return render(request, template_name='index.html', context=context)

def test(request):
    new = News.objects.all()
    allteam = Team.objects.all()
    context = {
        'e': request.session.get('my_email', ''),
        'new': new,
        'allteam': allteam
    }
    return render(request, template_name='test.html', context=context)


def signin(request):

    context = {
        'e': request.session.get('my_email', ''),
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
        'e': request.session.get('my_email', ''),
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

