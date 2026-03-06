from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    employee_id=models.CharField(max_length=100,unique=True)
    employee_first_name=models.CharField(max_length=100)
    employee_last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    def __str__(self):
        return f"{self.employee_first_name} {self.employee_last_name}"
class EmployeeWork(models.Model):
    work_id=models.CharField(max_length=100,unique=True)
    employee=models.ForeignKey(EmployeeDetails,on_delete =models.CASCADE,related_name='work')
    role=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    office_location=models.CharField(max_length=100)
    projects=models.JSONField(default=list)
    no_of_projects_completed=models.IntegerField()
    rating=models.FloatField()
    performance_summary=models.TextField()
    def __str__(self):
      return f"{self.employee.employee_first_name} - {self.role}"
    
    
    

