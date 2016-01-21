from django.contrib import admin

from .models import Client, Location, AttendanceRecord
# Register your models here.

admin.site.register(Client)
admin.site.register(Location)
admin.site.register(AttendanceRecord)