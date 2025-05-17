from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from Shopping.models.customer import Customer


class Userprofile(View):
    def get(self, request):
        customer_id = request.session.get('customer')
        if not customer_id:
            return redirect('login')  # or some other page if not logged in

        # Get only the current customer
        customer = get_object_or_404(Customer, pk=customer_id)

        return render(request, 'userprofile.html', {'customer': customer})

def update_profile(request, id):
    if request.method == 'POST':
        pi = Customer.objects.get(pk=id)
        fm = updatecustomer(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('userprofile')
        else:
            pi = Customer.objects.get(pk=id)
            fm = updatecustomer(instance=pi)
    else:
        pi = Customer.objects.get(pk=id)
        fm = updatecustomer(instance=pi)
    return render(request, 'updateprofile.html', {'form': fm})








"""
class Userprofile(View):
    def get(self, request):
        customer = request.session.get('customer')
        profile = Profile.get_profile_by_customer(customer)
        all_customer = Customer.get_all_customers();
        print(profile)
        return render(request, 'userprofile.html', {'profile': profile, 'all_customer': all_customer})
"""








