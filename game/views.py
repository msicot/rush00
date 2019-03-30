from django.shortcuts import render, HttpResponse

def index(request):
    if request.method == 'POST':
        r = request.POST['action']
        if r: 
            if  r == 'A':
                return render(request, 'game/map.html')
    return render(request, 'game/index.html')

# Create your views here.
