from django.urls import path
from .views import add_appointment, department_list, doctor_list

app_name = 'core_api'

urlpatterns = [
    path('add-appoinment/', add_appointment, name='add_appointment'),
    path('departments/', department_list, name='department_list'),
    path('doctors/', doctor_list, name='doctor_list'),

]

