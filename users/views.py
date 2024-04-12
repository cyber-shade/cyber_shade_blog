from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User
# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if not request.method == 'POST':
        return render(request, 'login.html')

    user = authenticate(
        request, username=request.POST['username'], password=request.POST['password'])

    if user is None:
        error_message = "the combination of username and password doesn't match!"
        return render(request, 'login.html', {'error_message': error_message})

    login(request, user)
    return redirect('profile')


def user_register(request):

    if request.user.is_authenticated:
        return redirect('profile')

    if not request.method == 'POST':
        return render(request, 'register.html')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    if User.objects.filter(username=username).exists():
        error_message = "the username exists"
        return render(request, 'register.html', {'error_message': error_message})

    if User.objects.filter(email=email).exists():
        error_message = "the email exists"
        return render(request, 'register.html', {'error_message': error_message})

    if password != password2:
        error_message = "the password doesn't match!"
        return render(request, 'register.html', {'error_message': error_message})

    try:
        user = User.objects.create_user(
            first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect('profile')
    except:
        error_message = 'somehting went wrong! try again.'
        return render(request, 'register.html', {'error_message': error_message})


@login_required
def profile(request):
    return render(request, 'profile.html')


def user_logout(request):
    next_page = request.GET.get('next', '/')
    logout(request)
    return redirect(next_page)
