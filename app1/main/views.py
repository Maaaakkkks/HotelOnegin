from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context: dict[str, str] = {
        'title': 'Отель Онегин - Главная',
        
    }
    
    return render(request, 'main/index.html', context)

def rooms(request):
    return render(request, 'main/rooms.html')

