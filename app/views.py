from django.shortcuts import render
from app.serializers import EmployeeMs
from app.models import Employee
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser


# Create your views here.



@api_view()
@permission_classes([IsAuthenticated])
def EmployeeData(request):
    EQS = Employee.objects.all()
    ESD = EmployeeMs(EQS,many = True)
    return Response(ESD.data)
    



