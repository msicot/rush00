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
            elif r == 'B':
                return redirect('/options/load_game')

        
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
    elif request.method == 'POST':
        move = request.POST['action']
        if move == 'start':
            return redirect('/options')
        elif move == 'select':
            settings.CURSOR_POS = 0
            return redirect('/moviedex')
    content = {
        'size': range(size),
        'position' : pos,
        'x' : pos % size ,
        'y' : pos // size,
        'scale' : scale,
    }
    if request.method == 'POST':
        r = request.POST['action']
        if r: 
            if  r == 'select':
                settings.CURSOR_POS = 0
                # Permet de rediriger lorsque il y a changement d'url
                return redirect('moviedex')
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