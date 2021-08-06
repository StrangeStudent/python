from django.shortcuts import render

from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'phonebook/home.html'
