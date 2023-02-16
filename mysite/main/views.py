from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from main.models import Aplikacija


## Create your views here.
class AplikacijaList(ListView):
    model=Aplikacija
    def get_queryset(self):
        selected_value = self.request.GET.get('aplikacija_AkGod')
        if selected_value:
            queryset = Aplikacija.objects.filter(aplikacija_AkGod=selected_value)
        else:
            queryset = Aplikacija.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_value = self.request.GET.get('aplikacija_AkGod')
        context['selected_value'] = selected_value
        context['ak_god'] = Aplikacija.objects.order_by("aplikacija_AkGod").values_list('aplikacija_AkGod', flat=True).distinct()
        return context

class AplikacijaPregledList(ListView):
    template_name='main/aplikacijaPregled_list.html'
    def get_queryset(self):
        self.aplikacija_naziv=get_object_or_404(Aplikacija, aplikacija_naziv=self.kwargs['aplikacija_naziv'])
        return Aplikacija.objects.filter(aplikacija_naziv=self.aplikacija_naziv)