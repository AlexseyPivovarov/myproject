from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView


# Create your views here.
# def base(request):
#     return HttpResponse('Hello world')
class HomeView(TemplateView):

    template_name = "base.html"

