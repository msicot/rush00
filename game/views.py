from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from random import randint
import os, subprocess, logging, ipdb
import common.data_manager as manager
import random

# Create your views here.

# replace by call class DataManager
def create_config(filename):
    print("\tcreating file...")
    if os.path.isfile(filename):
        print("REMOVE {}".format(filename))
        os.remove(filename)
    game_log = {'size': settings.GAME_CONFIG['size'],
                'first_position': settings.GAME_CONFIG['first_position'],
                'current_position' :0,
                'x': 0,
                'y': 0,
                'scale': '',
                'event': '',
                'movieball': 0,
    }
    print(game_log)
    # replace by call class DataManager
    manager.pickle_dump(game_log, filename)

def index(request):
    create_config('common/game_log.pickle')
    if request.method == 'POST':
        r = request.POST['action']
        if r: 
            if  r == 'A':
                # Permet de rediriger lorsque il y a changement d'url
                return redirect('worldmap')
    return render(request, 'game/index.html')

def worldmap(request):
    def event():
        return random.choice(['movieball', 'moviemon'])
    
    filename = 'common/game_log.pickle'
    if not os.path.isfile(filename):
        print("worldmap: creating file")
        create_config(filename)
    scale = ''
    action = ['haut', 'bas', 'droite', 'gauche']
    # replace by call class DataManager
    data = manager.pickle_load(filename)
    print(data)
    #ipdb.set_trace()
    size = data['size']
    pos = data['current_position']
    if request.method == 'POST' and any(x == request.POST['action'] for x in action):
        move = request.POST['action']
        if move == 'haut':
            pos = pos - size if (pos - size) // size  >= 0 else pos
            scale = "rotate(90deg)"
        elif move == 'bas':
            pos = pos + size if (pos + size) // size < size else pos
            scale = "rotate(-90deg)"
        elif move == 'droite':
            pos = pos + 1 if (pos) % size < size - 1 else pos
            scale = "ScaleX(-1)"
        elif move == 'gauche':
            pos = pos - 1 if pos % size != 0  else pos
            scale = "ScaleX(1)"
    data.update(
        current_position=pos if pos != data else data['current_position'],
        x = pos % size,
        y = pos // size,
        scale = scale,
        event = event(),
    ) 
    if data['event'] == 'moviemon':
        pass
    elif data['event'] == 'movieball':
        pass

    manager.pickle_dump(data, filename)
    data['size'] = range(size)
    print(data)
    return render(request, 'game/map.html', data)

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
