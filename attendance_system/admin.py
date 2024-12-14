from django.contrib import admin
from .models import Employee, Leave, LateArrival

# Admin panelinde modelleri kaydediyoruz
admin.site.register(Employee)
admin.site.register(Leave)
admin.site.register(LateArrival)
