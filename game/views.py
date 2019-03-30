from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings

def index(request):
    if request.method == 'POST':
        r = request.POST['action']
        if r: 
            if  r == 'A':
                # Permet de rediriger lorsque il y a changement d'url
                return redirect('worldmap')
    return render(request, 'game/index.html')

def worldmap(request):
    action = ['haut', 'bas', 'droite', 'gauche']
    print(settings.GAME_CONFIG['current_position'])
    size = settings.GAME_CONFIG['size']
    pos = settings.GAME_CONFIG['current_position'] or settings.GAME_CONFIG['first_position']
    if request.method == 'POST' and any(x == request.POST['action'] for x in action):
        move = request.POST['action']
        if move == 'haut':
          
            print('moving up')
            pos = pos - size if (pos - size) // size  >= 0 else pos
        elif move == 'bas':
            print('moving bas')
            pos = pos + size if (pos + size) // size < size else pos
        elif move == 'droite':
            print('moving droite')
            pos = pos + 1 if (pos) % size < size - 1 else pos
        elif move == 'gauche':
            print('moving gauche')
            pos = pos - 1 if pos % size != 0  else pos
    content = {
        'size': range(size),
        'position' : pos,
        'x' : pos % size ,
        'y' : pos // size,
    
    }
    settings.GAME_CONFIG['current_position'] = pos
    print("x ={}, y={}, pos={}".format(content['x'], content['y'], content['position']))
    return render(request, 'game/map.html', content)
