from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from main.models import *


## Create your views here.
class AplikacijaList(ListView):
    model=Aplikacija
