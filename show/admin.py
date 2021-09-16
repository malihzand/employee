from django.contrib import admin
from .models import AvailableJobs, employee

@admin.register(employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'email_id', 'phone_num', ]

@admin.register(AvailableJobs)
class AvailableJobsAdmin(admin.ModelAdmin):
    list_display=['name',]
