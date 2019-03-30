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
    print("Worldmap function")
    content = {
        'size': range(settings.GAME_CONFIG['size']),
    
    }
    return render(request, 'game/map.html', content)
