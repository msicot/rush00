from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings

# Create your views here.

def index(request):
    if request.method == 'POST':
        r = request.POST['action']
        if r: 
            if  r == 'A':
                # Permet de rediriger lorsque il y a changement d'url
                return redirect('worldmap')
    return render(request, 'game/index.html')

def worldmap(request):
    content = {
        'size': range(settings.GAME_CONFIG['size']),
    }
    return render(request, 'game/map.html', content)

# def moviedex(request):
#     return (HttpResponse("moviedex"))

def options(request):
    if request.method == 'POST':
        r = request.POST['action']
        if r: 
            if  r == 'A':
                return redirect('/options/save_game')
            elif r == 'B':
                return redirect('worldmap')
            elif r == 'start':
                return redirect('/')
    return render(request, 'game/options.html')

def save_game(request):
    if request.method == 'POST':
        r = request.POST['action']
        if r: 
            if  r == 'A':
                return (HttpResponse('DEV'))
            elif r == 'B':
                return redirect('/options')
            if r == 'bas':
                print(request.POST)
    mooc = [
        {'case': 'A', 'target' : True},
        {'case': 'B', 'target' : False},
        {'case': 'C', 'target' : False},
    ]
    return render(request, 'game/save_game.html', {'slots' : mooc})

def load_game(request):
    return (HttpResponse("loadgame"))