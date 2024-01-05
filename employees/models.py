from django.db import models

class Employee(models.Model):
    employee_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    department = models.CharField(max_length=50)
    salary = models.PositiveIntegerField()
    
    def __str__(self):
        return f'Employee: {self.first_name} {self.last_name}'



