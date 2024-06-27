
import contextlib
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm, Booking
from django.contrib import auth, messages
from django.urls import reverse



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
      
    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)





def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
      
    context = {
        'title': 'Авторизация',
        'form': form, 
    }
    return render(request, 'users/registration.html', context)






def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user), Booking(instance=request.user)
      
    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/profile.html', context)





def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))

