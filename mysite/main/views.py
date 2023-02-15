from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from main.models import *


## Create your views here.
class AplikacijaList(ListView):
    model=Aplikacija

class AplikacijaPregledList(ListView):
    template_name='main/aplikacijaPregled_list.html'
    def get_queryset(self):
        self.aplikacija_naziv=get_object_or_404(Aplikacija, aplikacija_naziv=self.kwargs['aplikacija_naziv'])
        return Aplikacija.objects.filter(aplikacija_naziv=self.aplikacija_naziv)