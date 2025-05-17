from Booking.models.booking import Booking
from django.shortcuts import render
from django.views import View


class all_booking(View):
    def get(self, request):
        customer = request.session.get('customer')
        booking_list = Booking.get_bookings_by_customer(customer)
        print(booking_list)
        return render(request, 'booked.html', {'booking_list': booking_list})

    def post(self, request):
        return render(request, 'orders.html')


"""
def get(self, request):
        customer = request.session.get('customer')
        booking_list = Booking.get_bookings_by_customer(customer)
        print(booking_list)
        return render(request, 'booked.html', {'booking_list': booking_list})"""