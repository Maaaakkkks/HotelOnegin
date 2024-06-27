from django.contrib import admin

# Register your models here.

from booking.models import Rooms, Booking

admin.site.register(Rooms)
admin.site.register(Booking)
# admin.site.register(Rooms_descript)