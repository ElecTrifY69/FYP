from django.shortcuts import render
from django.http import HttpResponse
from Infofutsal.models import Contact
from django.contrib import messages
from Shopping.models.customer import Customer
from Infofutsal.models.review import Review


# Create your views here.
def aboutus(request):
    #customer = Customer.get_all_customers();
    review = Review.get_all_reviews();
    return render(request, 'aboutus.html', {'review': review})
