import re
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Account
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data.get('password')
            password1 = form.cleaned_data.get('password1')
            if password != password1:
                message = '密碼不一致'
                return render(request, 'account/register.html', locals())
            user = Account.objects.create_user(username=username, email=email, password=password)
            user.is_active = True
            user.phone_number = phone_number
            user.save()
 
            return redirect('login') 
    else:
        form = RegisterForm()
    context = {
        "form":form,
    }
    return render(request, 'account/register.html', context)


def userlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            msg = "信箱或密碼錯誤"
            return render(request, 'account/login.html', locals())
    return render(request, 'account/login.html', locals())

@login_required
def userlogout(request):
    logout(request)
    return redirect('login')

def forgetpassword(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email=email)
        msg = "信箱或使用者帳號錯誤"
        if user.username == username:
            return redirect('updatepassword')
        
    return render(request, 'account/forgetpassword.html', locals())

def updatepassword(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        pwd1 = request.POST.get('password1')
        if pwd != pwd1:
            msg = "兩次密碼不一致"
            return render(request, 'account/updatepassword.html', locals())
        user = Account.objects.get(email=email)
        user.set_password(pwd)
        user.save()
        return redirect('login')
    return render(request, 'account/updatepassword.html', locals())