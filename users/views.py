from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .utils import url_message
from .models import CustomUser
# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if not request.method == 'POST':
        return redirect('/')

    user = authenticate(
        request, username=request.POST['username'], password=request.POST['password'])

    if user is None:
        url = url_message(
            request, 'نام کاربری یا رمز عبور اشتباه است', 'error')
        return redirect(url)

    login(request, user)
    url = url_message(request, 'با موفقیت وارد شدید ', 'success')
    return redirect(url)


def user_register(request):

    if request.user.is_authenticated:
        url = url_message(request, 'قبلاً وارد شدید', 'error')
        return redirect(url)

    if not request.method == 'POST':
        return redirect('/')
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    if CustomUser.objects.filter(username=username).exists():
        url = url_message(request, 'نام کاربری وجود دارد', 'error')
        return redirect(url)

    if CustomUser.objects.filter(email=email).exists():
        url = url_message(request, 'ایمیل وجود دارد', 'error')
        return redirect(url)
    if password != password2:
        url = url_message(request, 'رمز های عبور با هم مطابقت ندارد', 'error')
        return redirect(url)
    try:
        user = CustomUser.objects.create_user(
            first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        user.save()
        login(request, user)
        url = url_message(request, 'حساب شما با موفقیت ایجاد شد ', 'success')
        return redirect(url)
    except:
        url = url_message(request, 'مشکلی ایجاد شد، دوباره سعی کنید', 'error')
        return redirect(url)


@login_required
def profile(request):
    return render(request, 'profile.html')


def user_logout(request):
    logout(request)
    url = url_message(request, 'شما خارج شدید', 'success')
    return redirect(url)
