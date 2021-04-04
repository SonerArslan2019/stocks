from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET
from learning.models import Product

@require_GET
def product(request, pk=None):
    queryset = Product.objects.get(pk=pk)
    content = {
        'product_detail' : queryset
    }
    return render(request=request, template_name='product/detail.html', context=content)


def products(request):
    queryset = Product.objects.all()[:2]
    content = {
        'products' : queryset
    }
    return render(request=request, template_name='product/list.html', context=content)


def product_archieve(request, year=None, month=None):

    queryset = Product.objects.filter(created__year=year, created__month=month)

    content = {
        'year': year,
        'month': month,
        'products': queryset
    }
    return render(request=request, template_name='product/archieve.html', context=content)
