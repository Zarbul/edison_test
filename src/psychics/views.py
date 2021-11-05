from django.http import JsonResponse
from django.shortcuts import render

from django.shortcuts import render
from pynames.generators.russian import PaganNamesGenerator

from src.psychics.forms import InputNumberForm
from .models import PsyController

psychics = PsyController()


def index(request):
    request.session['username'] = PaganNamesGenerator().get_name_simple()
    request.session['user_numbers'] = []
    print(request.session['username'])
    print(request.session.keys())
    return render(request, 'base.html')


def input_number(request):
    print(request.session.values())
    print(request.session['user_numbers'])
    # print(user_numbers)
    form = InputNumberForm()
    if request.method == 'POST':
        form = InputNumberForm(request.POST)
        if form.is_valid():
            return render(request, 'index.html', {'form': form})
        else:
            form = InputNumberForm()
    return render(request, 'index.html', {'form': form})


def prediction(request):
    username = request.session['username']
    user_number = int(request.POST['number'])
    request.session['user_numbers'].append(user_number)
    request.session.modified = True
    responce = {'username': username,
                'user_numbers': request.session['user_numbers'],
                'psychics': psychics.check_all(user_number)
                }
    print(user_number)
    print(responce)

    return render(request, 'list.html', {'responce': responce})
