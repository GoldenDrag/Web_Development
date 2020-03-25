from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from . import models
from .models import Category, Product


def list_products(request):
    products = Product.objects.order_by('-name')[:5]
    # output = '; '.join([p.name for p in products])
    # template = loader.get_template('api/list_products.html')
    context = {'product_list': products}
    # return HttpResponse(template.render(context, request))
    return render(request, 'api/list_products.html', context)


def get_product(request, product_id):
    # try :
    #     product = Product.objects.get(pk=product_id)
    # except Product.DoesNotExist:
    #     raise Http404("Product does not exist")
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'api/details.html', {'product': product})


def list_categories(request):
    categories = Category.objects.order_by('-name')[:5]
    return render(request, 'api/list_categories.html', {'category_list': categories})


def get_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'api/category_details.html', {'category': category})


def category_products(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'api/list_products.html', {'product_list': products})
