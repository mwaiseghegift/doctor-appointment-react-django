from django.urls import path
from .views import add_appointment

app_name = 'core_api'

urlpatterns = [
    path('add-appoinment/', add_appointment, name='add_appointment'),
]

