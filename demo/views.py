from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Remark, Contact
# Create your views here.
def index(request):
    if request.method == "POST":
        name=request.POST['name']
        company=request.POST['company']
        email=request.POST['email']
        mobile=request.POST['mobile']
        msg=request.POST['msg'] 
        contactus=Contact.objects.create(name=name, company=company, email=email, mobile=mobile, msg=msg)
        contactus.save()
        return redirect('/')

    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        uname = request.POST['username']
        mail = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create(username=uname, email=mail, password=cpassword)
                user.save()
                messages.info('user created')
                return redirect('login')
        else:
            messages.info('password not matching')
        return redirect('/')
            

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            sc = request.POST['password']
            newuser=User.objects.get(username=username,password=sc)
            request.session['username']=newuser.username
            return redirect('/')
        except User.DoesNotExist as e:
            messages.info(request, 'invalid data')


    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def developer(request):
    return render(request, 'developer.html')

def remark(request):
    if request.method == "POST":
        name=request.POST['name']
        phone=request.POST['phone']
        message=request.POST['message']
        remarks=Remark.objects.create(name=name, phone=phone, message=message)
        remarks.save()
        return redirect('/')

    return render(request, 'remark.html')   

def contact(request):
    return render(request, 'contact.html')

def pro(request):
    return render(request, 'pro.html')