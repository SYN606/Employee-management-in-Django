from django.db import models

class Department(models.Model):

    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model): 

    first_name = models.CharField(max_length = 100, null = False)
    last_name = models.CharField(max_length = 100)
    dept = models.ForeignKey(Department, on_delete = models.CASCADE)
    salary = models.IntegerField(default = 0)
    bonus = models.IntegerField(default = 0)
    phone = models.IntegerField(default = 0)
    hire_date = models.DateField()

    def __str__(self) -> str:
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)
        