from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.text import re_newlines

from user.models import User


# Create your views here.

def sign_up(request):
    ctx = {}
    if request.POST:
        data = request.POST
        username = data.get('username', None)
        password = data.get('password', None)
        password_confirmation = data.get('password_confirmation', None)
        phone = data.get('phone', None)
        if None in [username, password, password_confirmation, phone]:
            ctx['error'] = "Something is wrong"
            return render(request, 'auth/register.html', ctx)

        user = User.objects.filter(username=username).first()

        if user:
            ctx['error'] = "It's already exist"
            return render(request, 'auth/register.html', ctx)

        if data['password'] != data['password_confirmation']:
            ctx['error'] = "Passwords are not same"
            return render(request, 'auth/register.html', ctx)

        user = User.objects.create_user(username=username, phone=phone, password=password)
        login(request, user)
        authenticate(request)
        return redirect('home')



    return render(request, "auth/register.html", ctx)

def sign_in(request):
    ctx={}
    if request.POST:
        data = request.POST
        username = data.get('username', None)
        password = data.get('password', None)
        if None in [username, password]:
            ctx['error'] = "Something is wrong"
            return render(request, 'auth/login.html', ctx)

        user = User.objects.filter(username=username).first()
        if not user:
            ctx['error'] = "Username or password is wrong"
            return render(request, 'auth/login.html', ctx)

        if not user.check_password(password):
            ctx['error'] = "Username or password is wrong"
            return render(request, 'auth/login.html', ctx)

        login(request, user)
        return redirect('home')


    return render(request, 'auth/login.html', ctx)

# @login_required(login_url='')
def sign_out(request):
    logout(request)
    return redirect('regis')