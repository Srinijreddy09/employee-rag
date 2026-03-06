from rest_framework import serializers
from .models import EmployeeDetails, EmployeeWork
class EmployeeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeWork
        fields = '__all__'
class EmployeeDetailsSerializer(serializers.ModelSerializer):
    work = EmployeeWorkSerializer(many=True, read_only=True)
    class Meta:
        model = EmployeeDetails
        fields = '__all__'