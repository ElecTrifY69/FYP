from django.shortcuts import render
from django.http import HttpResponse
from Booking.models import Tournamentregister
from django.contrib import messages
from django.views import View
from Shopping.models.customer import Customer


# Create your views here.
class Tregistration(View):
    # def Tregistration(request):
    def post(self, request):
        # if request.method == "POST":
        register = Tournamentregister()
        name = request.POST.get('name')
        team_name = request.POST.get('team_name')
        address = request.POST.get('address')
        number = request.POST.get('number')
        captain_name = request.POST.get('captain_name')
        manager_name = request.POST.get('manager_name')
        one_player = request.POST.get('one_player')
        two_player = request.POST.get('two_player')
        three_player = request.POST.get('three_player')
        four_player = request.POST.get('four_player')
        five_player = request.POST.get('five_player')
        six_player = request.POST.get('six_player')
        seven_player = request.POST.get('seven_player')
        eight_player = request.POST.get('eight_player')
        jersey_color = request.POST.get('jersey_color')
        coach_name = request.POST.get('coach_name')
        register.name = name
        register.team_name = team_name
        register.address = address
        register.number = number
        register.captain_name = captain_name
        register.manager_name = manager_name
        register.one_player = one_player
        register.two_player = two_player
        register.three_player = three_player
        register.four_player = four_player
        register.five_player = five_player
        register.six_player = six_player
        register.seven_player = seven_player
        register.eight_player = eight_player
        register.jersey_color = jersey_color
        register.coach_name = coach_name
        register.save()
        messages.success(request, 'Your form have been successfully recorded. Thank You!')
        return render(request, 'Tregistration.html')

    def get(self, request):
        customer = Customer.get_all_customers();
        return render(request, 'Tregistration.html', {'customer': customer})


