from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.profile import Profile


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description']
    list_filter = ['name', ]


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'created_at']
    list_filter = ['first_name', 'email', 'created_at']


class AdminOrder(admin.ModelAdmin):
    list_display = ['fullname', 'phone', 'product', 'quantity', 'price', 'ordered_at']
    list_filter = ['fullname', 'phone', 'product', 'price', 'ordered_at']


class AdminProfile(admin.ModelAdmin):
    list_display = ['customer']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
admin.site.register(Profile, AdminProfile)
