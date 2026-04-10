from django.shortcuts import render
from .models import Category, Product


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)

    return render(
        request,
        'category_products.html',
        {
            'category': category,
            'products': products
        }
    )