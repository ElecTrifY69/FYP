from django.db import models
import datetime
from Shopping.models.customer import Customer


class Booking(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=True, blank=True)
    time = models.TimeField()
    date = models.DateField()
    playing_hours = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    booked_at = models.DateField(auto_now_add=True, blank=True, null=True)


    @staticmethod
    def get_booking_by_customer(customer_id):
        return Booking.objects.filter(customer=customer_id).booking_by('-date')

    @staticmethod
    def all_booking():
        return Booking.objects.all()

    def placeBooking(self):
        self.save()

    def __str__(self):
        return self.fullname

    def is_valid(self, *args, **kwargs):
        now = datetime.date.today()
        if now > self.date:
            return False
        return True

    def phoneisExists(self):
        if Booking.objects.filter(phone=self.phone):
            return True
            return False

    def timeisExists(self):
        if Booking.objects.filter(time=self.time):
            return True
            return False

    @staticmethod
    def get_bookings_by_customer(customer_id):
        return Booking.objects.filter(customer=customer_id)