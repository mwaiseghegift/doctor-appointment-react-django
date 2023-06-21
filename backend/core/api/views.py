from core.api.serializers import DepartmentSerializer, DoctorSerializer, AppointmentSerializer
from core.models import Department, Doctor, Appointment
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['POST'])
def add_appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

