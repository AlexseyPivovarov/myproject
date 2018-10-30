from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import Category, Product
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import Profile


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


def detail(request, pid):
    context = {}
    context['category'] = Category.objects.all()
    context['product'] = Product.objects.get(id=pid)
    return render(request, template_name='core/detail.html', context=context)


def sign_up(request):
    get_form = UserCreationForm()
    if request.method == 'POST':
        post_form = UserCreationForm(request.POST)
        if post_form.is_valid():
            username = post_form.cleaned_data['username']
            password = post_form.cleaned_data['password1']
            User.objects.create_user(username=username, password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        return render(request, 'registration.html', {'reg_form': get_form})


@login_required
def profile(request):
    user = request.user
    form = Profile(instance=user)
    if request.method == 'POST':
        form = Profile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'profile.html', {'form': form})


@login_required
def my_product(request):
    context = {}
    context['category'] = Category.objects.all()
    paginator = Paginator(Product.objects.filter(
                product_user__id=request.user.id).order_by('-product_datatime_creation').all(), 4)
    context['product'] = paginator.get_page(request.GET.get('page'))
    return render(request, template_name='core/home.html', context=context)

