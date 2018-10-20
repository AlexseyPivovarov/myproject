from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import Category, Product
from django.core.paginator import Paginator


# create your views here.
def home(request):
    context = {}
    context['category'] = Category.objects.all()
    # context['product'] = Product.objects.filter(product_vip=1).order_by('-product_datatime_creation').all()
    paginator = Paginator(Product.objects.filter(product_vip=1).order_by('-product_datatime_creation').all(), 4)
    context['product'] = paginator.get_page(request.GET.get('page'))
    return render(request, template_name='core/home.html', context=context)


def category_list(request, pid):
    context = {}
    context['category'] = Category.objects.all()
    # context['product'] = Product.objects.filter(product_category__id=pid).order_by('-product_datatime_creation').all()
    paginator = Paginator(Product.objects.filter(
                product_category__id=pid).order_by('-product_datatime_creation').all(), 4)
    context['product'] = paginator.get_page(request.GET.get('page'))
    return render(request, template_name='core/home.html', context=context)


def all_list(request):
    context = {}
    context['category'] = Category.objects.all()
    # context['product'] = Product.objects.order_by('-product_datatime_creation').all()
    paginator = Paginator(Product.objects.order_by('-product_datatime_creation').all(), 4)
    context['product'] = paginator.get_page(request.GET.get('page'))
    return render(request, template_name='core/home.html', context=context)


