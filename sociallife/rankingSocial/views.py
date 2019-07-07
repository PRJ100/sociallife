from django.shortcuts import render
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'rankingSocial/lista.html'
    context_object_name = 'contexto'
    def get_queryset(self):
        pass