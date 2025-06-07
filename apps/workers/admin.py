from django.contrib import admin

from apps.workers.models import *

# Register your models here.


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'worker', 'reservation_date', 'reservation_time', 'name','phone_number','state')  
    search_fields = ('worker__username', 'worker__first_name','worker__last_name')
    list_filter = ('state', 'reservation_date')
