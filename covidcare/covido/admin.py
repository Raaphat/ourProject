from django.contrib import admin

# Register your models here.

from .models import Profile, Doctor, Patient, Review, Message, Symptom, Prescription, ChestDetails

admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Review)
admin.site.register(Message)
admin.site.register(Symptom)
admin.site.register(Prescription)
admin.site.register(ChestDetails)