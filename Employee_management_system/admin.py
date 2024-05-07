from django.contrib import admin
from .models import CustomUser, SalarySlip, Notification

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(SalarySlip)
admin.site.register(Notification)