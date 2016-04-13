from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    account = models.ForeignKey(User)
    
    time_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%.5f, %.5f' % ( self.latitude, self.longitude )

