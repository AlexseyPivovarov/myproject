from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator

from .models import Category, Product


class ListViewMixin:
    template_name = None
    paginete_by = 4

    def get(self, request, **kwargs):
        context = {}
        context['category'] = Category.objects.all()
        context['product'] = Paginator(
            get_list_or_404(
                Product.objects.order_by('-product_datatime_creation').all(), **kwargs
            ), self.paginete_by
        ).get_page(request.GET.get('page'))
        return render(request, template_name='core/home.html', context=context)