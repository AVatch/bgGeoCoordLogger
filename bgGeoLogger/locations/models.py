from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Coordinates(models.Model):
    altitude = models.FloatField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    altitudeAccuracy = models.FloatField()
    accuracy = models.IntegerField()

    is_moving = models.BooleanField()
    
    account = models.ForeignKey(User)
    
    time_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%.5f, %.5f' % ( self.latitude, self.longitude )