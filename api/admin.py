from django.contrib import admin

from .models import Doctor, Specialization, Appointment, Service, Patient, Schedule

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Service)
admin.site.register(Specialization)
admin.site.register(Schedule)
