# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import datetime



class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('user', 'User')])

    class Meta:
        db_table = 'custom_user'


class SalarySlip(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='salary_slips')
    upload_date = models.DateTimeField(auto_now_add=True)
    slip_file = models.FileField(upload_to='salary_slips/')

    def __str__(self):
        return f"{self.user.username} - {self.upload_date.strftime('%Y-%m-%d')}"



class Notification(models.Model):
    subject = models.CharField(max_length=50, null=True, blank=True)
    detail = models.CharField(max_length=150, null=True, blank=True)
    upload_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.upload_date.strftime('%Y-%m-%d')}"
