from django.contrib import admin
from django.urls import path
from .views.shopping import Shopping
from .views.login import Login, logout
from .views.signup import Signup
from .views.cart import Cart
from .views.checkout import CheckOut, orders_pdf
from .views.orders import OrderView
from Shopping.middlewares.auth import auth_middleware
from .views.profile import Userprofile, update_profile
from .views.orders import KhaltiVerifyView, KhaltiRequestView , verify_payment

urlpatterns = [
    path('shopping', auth_middleware(Shopping.as_view()), name='shopping'),
    path('signup', Signup.as_view()),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', auth_middleware(CheckOut.as_view()), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('userprofile', auth_middleware(Userprofile.as_view()), name='userprofile'),
    path('update_profile/<int:id>', update_profile, name=''),
    path('orders_pdf', auth_middleware(orders_pdf), name='orders_pdf'),
    path("khalti-request/", KhaltiRequestView.as_view(), name="khaltirequest"),
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khaltiverify"),
    path('api/verify_payment',verify_payment,name='verify_payment')
]