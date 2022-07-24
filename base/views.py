from django.shortcuts import render
# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets go'},
    {'id': 2, 'name': 'Lets go go'},
    {'id': 3, 'name': 'Lets go go go'}
]

planck = 6.63


def home(request):
    context = {'rooms': rooms, 'planck': planck}
    return render(request, 'home.html', context)


def room(request):
    return render(request, 'room.html')
