from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from Shopping.models.customer import Customer


class futsalbooking(View):
    def get(self, request):
        customer = Customer.get_all_customers();
        print('you are: ', request.session.get('customer'))
        return render(request, 'futsalbooking.html' , {'customer': customer})
