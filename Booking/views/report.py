from django.shortcuts import render
from Booking.models.booking import Booking


def showreport(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchreport = Booking.objects.raw(
            'select id, fullname , date , time , playing_hours , booked_at from Booking_booking where booked_at between "' + fromdate + '" and "' + todate + '"')
        return render(request, 'report.html', {'data': searchreport})
    else:
        displaydata = Booking.objects.all()
        return render(request, 'report.html', {'data': displaydata})
