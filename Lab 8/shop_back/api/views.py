from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product
from .models import Category

# Create your views here.

def product_list(request):
    return JsonResponse(serialize_product_list(Product.objects.all()), 
                        safe=False)

def product(request, product_id):
    return JsonResponse(serialize_product(get_object_or_404(Product, id=product_id)), 
                        safe=True)

def category_list(request):
    return JsonResponse(serialize_category_list(Category.objects.all()), 
                        safe=False)

def category(request, category_id):
    return JsonResponse(serialize_category(get_object_or_404(Category, id=category_id)), 
                        safe=False)

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return JsonResponse(serialize_product_list(Product.objects.filter(category=category).all()), 
                        safe=False)


def serialize_product(product: Product):
    json_data = {}
    json_data['name'] = product.name
    json_data['price'] = product.price
    json_data['description'] = product.description
    json_data['count'] = product.count
    json_data['is_active'] = product.is_active
    return json_data

def serialize_product_list(products: list[Product]):
    return list(map(serialize_product, products))

def serialize_category(category: Category):
    return {'name': category.name}

def serialize_category_list(categories: list[Category]):
    return list(map(serialize_category, categories))