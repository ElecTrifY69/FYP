from django.contrib import admin
from .models.tregister import Tournamentregister
from .models.booking import Booking


# Register your models here.
class AdminTournamentregister(admin.ModelAdmin):
    list_display = ['name', 'team_name', 'address', 'number', 'captain_name', 'manager_name', 'jersey_color',
                    'coach_name']
    list_filter = ['name', 'team_name']


class AdminBooking(admin.ModelAdmin):
    list_display = ['fullname', 'phone', 'time', 'date', 'playing_hours', 'booked_at']
    list_filter = ['fullname', 'time', 'date', 'booked_at']


admin.site.register(Tournamentregister, AdminTournamentregister)
admin.site.register(Booking, AdminBooking)
