import json

from django import views
from django.shortcuts import render, redirect

from django.views import generic
from .models import Psychics

from src.psychics.forms import InputNumberForm


class InputNumberView(generic.FormView):
    template_name = 'index.html'
    form_class = InputNumberForm


def prediction(request):
    user_number = int(request.POST['number'])
    queryset = Psychics.objects.all()
    for psy in queryset:
        psy_num = psy.psy_num()
        all_psy_num = psy.all_numders
        if all_psy_num:
            all_psy_num = json.loads(all_psy_num)
        else:
            all_psy_num = []
        all_psy_num.append(psy_num)
        psy.all_numders = json.dumps(all_psy_num)
        print(all_psy_num)
        if user_number == psy_num:
            psy.credibility += 1
        psy.save()
    return redirect('/results/')


class ResultView(generic.ListView):
    model = Psychics
    template_name = 'list.html'

