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
            User.objects.get_or_create(fullname=fullname, email=email, phone=phone,
                                       password=make_password(password))
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
        elif check_user and not check_user[0].check_password(password):
            messages.error(request, 'Wrong Password')
            return redirect('auth_login')
        else:
            user = authenticate(request, email=email, password=password)
            login(request, user)
            messages.success(request, f'Welcome {email}')
            return redirect('home')
    return render(request, 'main/index.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def change_password_view(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if user.password != current_password:
            messages.error(request, 'Your current password is NOT correct')
            return redirect('home')
        elif new_password != confirm_password:
            messages.error(request, 'Password mismatched')
            return redirect('home')
        else:
            user.set_password(new_password)
            user.save()
            messages.success(
                request, 'Password was updated successfully, kindly login to continue')
            return redirect('auth_logout')
    return render(request, 'auth/index.html')
