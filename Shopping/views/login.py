from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from Shopping.models.customer import Customer
from django.views import View


class Login(View):
    return_url = None

    def get(self, request):
        customer = Customer.get_all_customers();
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html' , {'customer': customer})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                return redirect('homepage')
            else:
                error_message = 'Email or Password Invalid!'
        else:
            error_message = 'Email or Password Invalid!'
            print(email, password)
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('homepage')


