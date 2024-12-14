from django.shortcuts import render
from .models import Employee
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    Employees = Employee.objects.all()
    context = {
        'employees': Employees
    }
    return render(request, 'Employees/index.html', context)

@login_required
def employee_dashboard(request):
    return render(request, 'attendance/employee_dashboard.html')

@login_required
def manager_dashboard(request):
    if request.user.is_staff:  # Yetkili mi kontrol ediyoruz
        return render(request, 'attendance/manager_dashboard.html')
    else:
        return render(request, 'attendance/employee_dashboard.html')
