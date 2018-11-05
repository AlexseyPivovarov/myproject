from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from .forms import ProductForm
from .models import Category, Product
from .mixinviews import ListViewMixin


class HomeView(ListViewMixin, View):
    template_name = 'core/home.html'

    def get(self, request):
        return super().get(request=request, product_vip=1)


class CategoryListView(ListViewMixin, View):
    template_name = 'core/home.html'

    def get(self, request, pid):
        return super().get(request=request, product_category__id=pid)


class MyProductView(ListViewMixin, View):
    template_name = 'core/home.html'

    def get(self, request):
        return super().get(request=request, product_user__id=request.user.id)


class AllListView(ListViewMixin, View):
    template_name = 'core/home.html'

    def get(self, request):
        return super().get(request=request)


class MyDetailView(View):

    def get(self, request, pid):
        context = {}
        context['category'] = Category.objects.all()
        context['product'] = get_object_or_404(Product, id=pid)
        return render(request, template_name='core/detail.html', context=context)


# @login_required
# def add_product(request):
#     user = request.user
#     form = ProductForm(instance=user)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#     return render(request, 'core/add.html', {'form': form})
class AddProduct(View):

    def get(self, request):
        return render(request, 'core/add.html', {'form': ProductForm()})

    def post(self, request):
        form = ProductForm(request.POST, instance=Product(product_user=request.user))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

