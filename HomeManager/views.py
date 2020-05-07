from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.
class Home(TemplateView):
    template_name = 'HomeManager/HomePage.html'
