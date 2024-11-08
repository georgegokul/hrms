from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('all_emp', views.all_emp, name='all_emp'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('api/add-employee/', views.add_employee, name='add_employee'),
    path('api/get-all-employees/', views.get_all_employees, name='get_all_employees'),
    path('api/mark-attendance/<int:employee_id>/', views.mark_attendance, name='mark_attendance'),
    path('api/get-attendance/<int:employee_id>/', views.get_attendance, name='get_attendance'),
    path('emp-attendance/', views.employee_attendance_detail),
]