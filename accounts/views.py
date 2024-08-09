from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from .models import CustomUser as User


def register_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        else:
            new_user = User.objects.get_or_create(fullname=fullname, email=email, phone=phone,
                                                  password=make_password(password))
            if new_user:
                user = authenticate(
                    request, email=email, password=password)
                login(request, user)
        return redirect('home')
    return render(request, 'main/index.html', {})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        check_user = User.objects.filter(email=email)
        if not check_user:
            messages.error(request, f'User with "{email}" does not exist')
            return redirect('home')
        else:
            user = authenticate(request, email=email, password=password)
            login(request, user)
            messages.success(request, f'Welcome {email}')
            return redirect('home')
    return render(request, 'main/index.html')


def logout_view(request):
    logout(request)
    return redirect('home')
