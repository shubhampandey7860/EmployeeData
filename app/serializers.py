from rest_framework import serializers
from app.models import Employee


class EmployeeMs(serializers.ModelSerializer):
    class Meta :
        model = Employee
        fields = '__all__'
        
        