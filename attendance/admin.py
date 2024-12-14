from django.contrib import admin
from .models import Employee, Leave, LateArrival

admin.site.register(Employee)
admin.site.register(Leave)
admin.site.register(LateArrival)
# Register your models here.
