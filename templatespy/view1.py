from django.shortcuts import render
from django.http import HttpResponseRedirect
from base.forms import NameForm
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


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
