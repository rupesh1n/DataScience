from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'department'

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    hire_date = models.DateField()
    exit_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'employee'

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_date = models.DateField()

    class Meta:
        db_table = 'performance'