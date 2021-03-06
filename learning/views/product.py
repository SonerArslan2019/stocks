from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET
from learning.models import Product
from django.views import View
from django.views.generic import ListView, DetailView


@require_GET
def product(request, pk=None):
    queryset = Product.objects.get(pk=pk)
    content = {
        'product_detail': queryset
    }
    return render(request=request, template_name='learning/product/detail.html', context=content)


def products(request):
    queryset = Product.objects.all()[:2]
    content = {
        'products': queryset
    }
    return render(request=request, template_name='learning/product/list.html', context=content)


def product_archieve(request, year=None, month=None):
    queryset = Product.objects.filter(created__year=year, created__month=month)

    content = {
        'year': year,
        'month': month,
        'products': queryset
    }
    return render(request=request, template_name='learning/product/archieve.html', context=content)


class ProductView(View):

    def get(self, request):
        product_list = Product.objects.all()[:2]
        content = {
            'products': product_list
        }
        return render(request=request, template_name='learning/product/list.html', context=content)

    def post(self, request):
        pass


class ProductListView(ListView):
    model = Product
    template_name = 'learning/product/list.html'
    context_object_name = 'products'
    queryset = Product.objects.all()[:2]  # kac tane urun gostermesini istersek ona gore rakam veririz


class ProductDetailView(DetailView):
    model = Product
    template_name = 'learning/product/detail.html'
    context_object_name = 'product_detail'
