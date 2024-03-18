# myapp/admin.py
from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'mobile_number', 'email', 'consulting_date', 'doctor_name')

# Register the Patient model with the custom admin class
admin.site.register(Patient, PatientAdmin)
