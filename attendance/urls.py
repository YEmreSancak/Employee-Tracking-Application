from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Create your views here.
urlpatterns = [
    path('', views.index, name='index'),
     # Login
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # Logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Personel Dashboard
    path('dashboard/employee/', views.employee_dashboard, name='employee_dashboard'),
    
    # Yetkili Dashboard
    path('dashboard/manager/', views.manager_dashboard, name='manager_dashboard'),
]