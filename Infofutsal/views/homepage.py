from django.shortcuts import render
from django.http import HttpResponse
from Infofutsal.models import Contact
from django.contrib import messages
from Shopping.models.customer import Customer


# Create your views here.
def firsthomepage(request):
    customer = Customer.get_all_customers();
    return render(request, 'firsthomepage.html', {'customer': customer})
