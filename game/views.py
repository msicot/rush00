from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from random import randint

# Create your views here.

def index(request):
    def set_var():
        settings.GAME_CONFIG['current_position'] = 0

    set_var()
    if request.method == 'POST':
        r = request.POST['action']
        if r: 
            if  r == 'A':
                # Permet de rediriger lorsque il y a changement d'url
                return redirect('worldmap')
    return render(request, 'game/index.html')

def worldmap(request):
    scale = ''
    action = ['haut', 'bas', 'droite', 'gauche']
    print(settings.GAME_CONFIG['current_position'])
    size = settings.GAME_CONFIG['size']
    pos = settings.GAME_CONFIG['current_position'] or settings.GAME_CONFIG['first_position']
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
    content = {
        'size': range(size),
        'position' : pos,
        'x' : pos % size ,
        'y' : pos // size,
        'scale' : scale,
    }
    settings.GAME_CONFIG['current_position'] = pos
    print("x ={}, y={}, pos={}".format(content['x'], content['y'], content['position']))
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

def moviedex(request):
    movies = {
        "movie 1": "img_a",
        "movie 2": "img_b",
        "movie 3": "img_c",
        "movie 4": "img_d",
        "movie 5": "img_e",
    }
    #pos = 0
    if request.method == 'POST':
        r = request.POST['action']
        if r:
            if r == 'bas' and settings.CURSOR_POS < len(movies) - 1:
                settings.CURSOR_POS += 1
            if r == 'haut' and settings.CURSOR_POS - 1 >= 0:
                settings.CURSOR_POS -= 1
    print(settings.CURSOR_POS, len(movies))
    return render(request, 'game/moviedex.html', {'movies': movies, 'pos': settings.CURSOR_POS })