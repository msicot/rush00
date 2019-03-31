from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
import os
import subprocess
import logging
from common.data_manager import DataManager as manager
import random


def index(request):
    manager('common/game_log.pickle').load_default_settings()
    if request.method == 'POST':
        r = request.POST['action']
        if r:
            if r == 'A':
                # Permet de rediriger lorsque il y a changement d'url
                return redirect('worldmap')
            elif r == 'B':
                return redirect('/options/load_game')

        
    return render(request, 'game/index.html')


def worldmap(request):
    def event(game):
        return random.choice(['movieball', 'moviemon']) if game == True else ''

    filename = 'common/game_log.pickle'
    if not os.path.isfile(filename):
        manager(filename).load_default_settings()
        print("worldmap: creating file")
    scale = ''
    action = ['haut', 'bas', 'droite', 'gauche']
    # replace by call class DataManager
    data = manager(filename).load()
    #print(data)
    # ipdb.set_trace()
    size = data['size']
    pos = data['current_position']
    if request.method == 'POST' and any(x == request.POST['action'] for x in action):
        move = request.POST['action']
        if move == 'haut':
            pos = pos - size if (pos - size) // size >= 0 else pos
            scale = "rotate(90deg)"
        elif move == 'bas':
            pos = pos + size if (pos + size) // size < size else pos
            scale = "rotate(-90deg)"
        elif move == 'droite':
            pos = pos + 1 if (pos) % size < size - 1 else pos
            scale = "ScaleX(-1)"
        elif move == 'gauche':
            pos = pos - 1 if pos % size != 0 else pos
            scale = "ScaleX(1)"
        elif move == 'start':
            return redirect('/options')
        elif move == 'select':
            settings.CURSOR_POS = 0
            return redirect('/moviedex')

    data.update(
        current_position=pos if pos != data else data['current_position'],
        x=pos % size,
        y=pos // size,
        scale=scale,
        event=event(data['start'])
    )
    data.update(start=True)
    if data['event'] == 'moviemon':
        data['moviemon_found'] = manager(
            filename).get_random_movie(data['moviemon_db'])
    elif data['event'] == 'movieball':
        data['movieball'] += 1
    manager(filename).dump(data)
    data['size'] = range(size)
    print(data)
    return render(request, 'game/map.html', data)


def battle(request):
    print("Battle !")
    filename = 'common/game_log.pickle'
    data = manager(filename).load()
    # moviemon_list = settings.GAME_CONFIG['moviemon']
    # movie_index = randint(0, len(moviemon_list) - 1)
    # movie_content = {**moviemon_list[movie_index]}
    # print(movie_content)
    data['moviemon_found'] = manager(filename).get_random_movie(data['moviemon_db'])
    if request.method == 'POST':
        r = request.POST['action']
        if r:
            if r == 'B':
                # Permet de rediriger lorsque il y a changement d'url
                return redirect('worldmap')

    return render(request, 'game/battle.html', data['moviemon_found'])

# def moviedex(request):
#     return (HttpResponse("moviedex"))


def options(request):
    if request.method == 'POST':
        r = request.POST['action']
        if r:
            if r == 'A':
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
            if r == 'A':
                return (HttpResponse('DEV'))
            elif r == 'B':
                return redirect('/options')
            if r == 'bas' and settings.CURSOR_POS < 2:
                settings.CURSOR_POS += 1
            elif r == 'haut' and settings.CURSOR_POS > 0:
                settings.CURSOR_POS -= 1
    mooc = [
        {'case': 'A', 'target': True},
        {'case': 'B', 'target': False},
        {'case': 'C', 'target': False},
    ]
    count = 0
    while count < 3:
        if count == settings.CURSOR_POS:
            mooc[count]['target'] = True
        else:
            mooc[count]['target'] = False
        count += 1
    return render(request, 'game/save_game.html', {'slots' : mooc})

def load_game(request):
    if request.method == 'POST':
        r = request.POST['action']
        if r: 
            if  r == 'A':
                return (HttpResponse('DEV'))
            elif r == 'B':
                return redirect('/options')
            if r == 'bas' and settings.CURSOR_POS < 2:
                settings.CURSOR_POS += 1
            elif r == 'haut' and settings.CURSOR_POS > 0:
                settings.CURSOR_POS -= 1
    mooc = [
        {'case': 'A', 'target' : True},
        {'case': 'B', 'target' : False},
        {'case': 'C', 'target' : False},
    ]
    count = 0
    while count < 3:
        if count == settings.CURSOR_POS:
            mooc[count]['target'] = True
        else:
            mooc[count]['target'] = False
        count += 1
    return render(request, 'game/load_game.html', {'slots' : mooc})

def info_movie(request):
    moviemon_list = settings.GAME_CONFIG['moviemon']
    movie_index = randint(0, len(moviemon_list) - 1)
    movie_content = {**moviemon_list[movie_index]}
    return render(request, 'game/info_movie.html', movie_content)

def moviedex(request):
    movies = {
        "movie 1": "img_a",
        "movie 2": "img_b",
        "movie 3": "img_c",
        "movie 4": "img_d",
        "movie 5": "img_e",
        "movie 11": "img_a",
        "movie 22ddddddddddddddddd": "img_b",
        "movie 33": "img_c",
        "movie 44": "img_d",
        "movie 55": "img_e",
        "movie 111": "img_a",
        "movie 222": "img_b",
        "movie 333": "img_c",
        "movie 444": "img_d",
        "movie 555": "img_e",
    }
    #pos = 0
    if request.method == 'POST':
        r = request.POST['action']
        if r:
            if r == 'bas' and settings.CURSOR_POS < len(movies) - 1:
                settings.CURSOR_POS += 1
            if r == 'haut' and settings.CURSOR_POS - 1 >= 0:
                settings.CURSOR_POS -= 1
            #if r == ''
            if  r == 'select':
                # Permet de rediriger lorsque il y a changement d'url
                return redirect('worldmap')
    print(settings.CURSOR_POS, len(movies))
    return render(request, 'game/moviedex.html', {'movies': movies, 'pos': settings.CURSOR_POS})
