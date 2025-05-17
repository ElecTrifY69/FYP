from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from Shopping.models.customer import Customer
from django.views import View
from Shopping.models.product import Product


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})

    def post(self, request):
        return render(request, 'orders.html')
