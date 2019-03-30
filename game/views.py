from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from random import randint

def index(request):
    if request.method == 'POST':
        r = request.POST['action']
        if r: 
            if  r == 'A':
                # Permet de rediriger lorsque il y a changement d'url
                return redirect('worldmap')
    return render(request, 'game/index.html')

def worldmap(request):
    print("Worldmap function")

    if request.method == 'POST':
        r = request.POST['action']
        if r: 
            if  r == 'B':
                # Permet de rediriger lorsque il y a changement d'url
                return redirect('battle')

    content = {
        'size': range(settings.GAME_CONFIG['size']),
    
    }
    return render(request, 'game/map.html', content)

def battle(request):
    print("Battle !")
    moviemon_list = settings.GAME_CONFIG['moviemon']
    movie_index = randint(0, len(moviemon_list) - 1)
    movie_content = {**moviemon_list[movie_index]}
    print(movie_content)

    if request.method == 'POST':
        r = request.POST['action']
        if r: 
            if  r == 'B':
                # Permet de rediriger lorsque il y a changement d'url
                return redirect('worldmap')

    return render(request, 'game/battle.html', movie_content)

