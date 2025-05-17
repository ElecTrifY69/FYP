from django.db import models


class Tournamentregister(models.Model):
    name = models.CharField(max_length=150)
    team_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    number = models.CharField(max_length=150)
    captain_name = models.CharField(max_length=150)
    manager_name = models.CharField(max_length=150)
    one_player = models.CharField(max_length=150)
    two_player = models.CharField(max_length=150)
    three_player = models.CharField(max_length=150)
    four_player = models.CharField(max_length=150)
    five_player = models.CharField(max_length=150)
    six_player = models.CharField(max_length=150)
    seven_player = models.CharField(max_length=150)
    eight_player = models.CharField(max_length=150)
    jersey_color = models.CharField(max_length=150)
    coach_name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
