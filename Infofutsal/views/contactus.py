from django.shortcuts import render
from Infofutsal.models import Contact
from django.contrib import messages
from django.views import View
from Shopping.models.customer import Customer


class contactus(View):
    def get(self, request):
        customer = Customer.get_all_customers();
        return render(request, 'contactus.html', {'customer':customer})

    def post(self, request):
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.phone = phone
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.success(request, 'Your message has been sent successfully!', extra_tags='contact')
        return render(request , 'contactus.html')
