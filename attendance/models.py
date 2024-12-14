from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('employee', 'Personel'),
        ('admin', 'Yetkili'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

    def __str__(self):
        return f'{self.username} - {self.role}'

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField(auto_now_add=True)  # İşe başlama tarihi
    annual_leave = models.PositiveIntegerField(default=15)  # Başlangıçta 15 gün izin verilecek

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=50)  # Örneğin, yıllık izin, hastalık izni vb.
    approval_status = models.BooleanField(default=False)  # Onay durumu

    def __str__(self):
        return f'{self.employee.first_name} {self.employee.last_name} - {self.leave_type}'


class LateArrival(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    late_time = models.DurationField()  # Geç kalma süresi
    date = models.DateField(auto_now_add=True)  # Geç kalma tarihi

    def __str__(self):
        return f'{self.employee.first_name} {self.employee.last_name} - {self.late_time}'
