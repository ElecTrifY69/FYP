from django.shortcuts import render, redirect, HttpResponseRedirect
from Booking.models.booking import Booking
from Booking.forms import AddBooking
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from Shopping.models.customer import Customer
from django.views import View
from django.core.mail import EmailMultiAlternatives
from datetime import datetime


class FutsalBooking(View):
    model = Booking
    template_name = 'booking.html'

    def get(self, request):
        customer = Customer.get_all_customers()
        time_options = [f"{(hour % 12) or 12}:00 {'AM' if hour < 12 else 'PM'}" for hour in range(7, 22)]
        print('You are: ', request.session.get('customer'))
        print('Time options:', time_options)
        return render(request, "booking.html", {'customer': customer, 'time_options': time_options})

    def post(self, request):
        fullname = request.POST.get('fullname')
        customer = request.session.get('customer')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        date = request.POST.get('date')
        time = request.POST.get('time')
        playing_hours = request.POST.get('playing_hours')
        time = datetime.strptime(time, "%I:%M %p").strftime("%H:%M")
        value = {
            'fullname': fullname,
            'email': email,
            'phone': phone,
            'address': address,
            'date': date,
            'time': time,
            'playing_hours': playing_hours,
            'customer': customer
        }
        error_message = None
        booking = Booking(fullname=fullname,
                          customer=Customer(id=customer),
                          email=email,
                          phone=phone,
                          address=address,
                          date=date,
                          time=time,
                          playing_hours=playing_hours)
        error_message = self.validateBooking(booking)
        if not error_message:
            print(fullname, phone, address, date, time, customer)
            request.session['booking'] = booking.id
            booking.save()
            subject = 'Futsal Booked Successfully!'
            from_email = 'Sirutarfutsal2018@gmail.com'
            to = [email]
            text_content = f'Hi {fullname}, your futsal booking is confirmed for {date} at {time} for {playing_hours} hours.'
            html_content = render_to_string('Userfutsalbooking_email.html', {
                'fullname': fullname,
                'date': date,
                'time': time,
                'playing_hours': playing_hours
            })

            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            admin_subject = 'New Futsal Booking Alert!'
            admin_email = ['akmbiplav@gmail.com']  # Add more admin emails if needed
            admin_text = f'New booking by {fullname} on {date} at {time} for {playing_hours} hours.\nContact: {phone}, Email: {email}'
            admin_html = render_to_string('Adminfutsalbooking_email.html', {
                'fullname': fullname,
                'email': email,
                'phone': phone,
                'address': address,
                'date': date,
                'time': time,
                'playing_hours': playing_hours
            })

            admin_msg = EmailMultiAlternatives(admin_subject, admin_text, from_email, admin_email)
            admin_msg.attach_alternative(admin_html, "text/html")
            admin_msg.send()

            return redirect('bookings')
        else:
            data = {
                'error': error_message,
                'values': value
            }
        return render(request, 'booking.html', data)

    def validateBooking(self, booking):
        error_message = None
        if (not booking.fullname):
            error_message = "Full Name Required!"
        elif len(booking.fullname) < 4:
            error_message = "Full Name must be 4 char long or more."
        elif not booking.address:
            error_message = "Address Required"
        elif len(booking.address) < 4:
            error_message = "Address must be 4 char long or more."
        elif not booking.phone:
            error_message = "Phone Number Required."
        elif len(booking.phone) < 10:
            error_message = "Phone Number must be 10 char long."
        elif booking.phoneisExists():
            error_message = "Phone Number is already registered."
        elif booking.timeisExists():
            error_message = "Futsal is Booked at this Time."
        return error_message


"""def all_booking(request):
    print(bookings)
    return render(request, 'booked.html', {'booking_list': booking_list})
"""

def add_booking(request):
    if request.method == 'POST':
        fm = AddBooking(request.POST)
        if fm.is_valid():
            fullname = fm.cleaned_data['fullname']
            phone = fm.cleaned_data['phone']
            address = fm.cleaned_data['address']
            date = fm.cleaned_data['date']
            time = fm.cleaned_data['time']
            playing_hours = fm.cleaned_data['playing_hours']
            reg = Booking(fullname=fullname, phone=phone, address=address, date=date, time=time,
                          playing_hours=playing_hours)
            reg.save()
            fm = AddBooking()
            return redirect('bookings')
    else:
        fm = AddBooking()
    return render(request, 'add_booking.html', {'form': fm})


def delete_booking(request, id):
    if request.method == 'POST':
        db = Booking.objects.get(pk=id)
        db.delete()
        return HttpResponseRedirect('/bookings')


def update_booking(request, id):
    if request.method == 'POST':
        pi = Booking.objects.get(pk=id)
        fm = AddBooking(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('bookings')
        else:
            pi = Booking.objects.get(pk=id)
            fm = AddBooking(instance=pi)
    else:
        pi = Booking.objects.get(pk=id)
        fm = AddBooking(instance=pi)
    return render(request, 'update_booking.html', {'form': fm})


def sendfutsalmail(request):
    send_mail(
        'New Futsal Time have been Booked!',
        'Hi , This is a mail to confirm that new Futsal Time have been booked. Please check admin dashboard and confirm the bookings.',
        'akmbiplav@gmail.com',
        ['akmbiplav@gmail.com'],
        fail_silently=False,
    )
    return redirect('bookings')
