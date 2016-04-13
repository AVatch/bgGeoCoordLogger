from django.contrib import admin

from .models import Coordinates

class CoordinatesAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'account')
    list_display_links = ('id',)
admin.site.register(Coordinates, CoordinatesAdmin)
