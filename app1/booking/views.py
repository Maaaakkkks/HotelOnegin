from django.shortcuts import render
from booking.forms import Booking
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def booking1(request):
    if request.method == 'POST':
        form = Booking(data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('users:profile'))    
    return render(request, 'users/profile.html')

def booking2(request):
    if request.method == 'POST':
        form = Booking(data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('users:profile'))
    return render(request, 'users/profile.html')

def booking3(request):
    if request.method == 'POST':
        form = Booking(data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('users:profile'))
    return render(request, 'users/profile.html')

def booking4(request):
    if request.method == 'POST':
        form = Booking(data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('users:profile'))
    return render(request, 'users/profile.html')

def booking5(request):
    if request.method == 'POST':
        form = Booking(data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('users:profile'))
    return render(request, 'users/profile.html')

def booking6(request):
    if request.method == 'POST':
        form = Booking(data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('users:profile'))
    return render(request, 'users/profile.html')