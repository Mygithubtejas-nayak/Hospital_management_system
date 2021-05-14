from django.contrib import admin

# Register your models here.
from .models import Patient, Receptionist, Doctor, Appointment, Inventory_item, Bills

admin.site.register(Patient)
admin.site.register(Receptionist)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Inventory_item)
admin.site.register(Bills)
