from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Category, Product


class ListViewMixin:
    template_name = None
    paginete_by = 4

    def get(self, request, my_filter):
        context = {}
        context['category'] = Category.objects.all()
        context['product'] = Paginator(Product.objects.filter(**my_filter).order_by('-product_datatime_creation').all(),
                                       self.paginete_by).get_page(request.GET.get('page'))
        return render(request, template_name='core/home.html', context=context)