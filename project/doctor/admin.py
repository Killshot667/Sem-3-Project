from django.contrib import admin
from .models import Contact,Doctor,Speciality
# Register your models here.

admin.site.register(Contact)
admin.site.register(Speciality)
admin.site.register(Doctor)
