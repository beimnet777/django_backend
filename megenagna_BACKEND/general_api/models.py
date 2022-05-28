from django.db import models
from django.contrib.auth.models import User
from numpy import size

# Create your models here.
class EmployeeProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    employee_name = models.CharField(max_length=100)
    employee_age = models.IntegerField()
    employee_specialization = models.CharField(max_length = 100)
    employee_description = models.TextField()
    employee_gpa = models.FloatField(max_length=3)
    employee_degree_name = models.CharField(max_length=70)
    skills_1=models.CharField(max_length=60)
    skills_2=models.CharField(max_length=60)
    skills_3=models.CharField(max_length=60)
    skills_4=models.CharField(max_length=60)
    sex=models.CharField(max_length=10)

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    employer_name = models.CharField(max_length=100)
    employer_city=models.CharField(max_length=60)
    employer_sub_city=models.CharField(max_length=60)
    employer_function = models.CharField(max_length = 100)

class Job(models.Model):
<<<<<<< HEAD
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job_name = models.CharField(max_length= 100)
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length= 100)
>>>>>>> 55ed49dd74fa31f0d6fdcf69bd9e20665540dedc
    job_experience_years = models.IntegerField()
    job_description = models.TextField()
    job_benefits=models.TextField()
    job_salary=models.IntegerField()
    skills_needed_1=models.CharField(max_length=60)
    skills_needed_2=models.CharField(max_length=60)
    skills_needed_3=models.CharField(max_length=60)
    skills_needed_4=models.CharField(max_length=60)
class Application(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, null=True)
    gpa=models.FloatField(max_length=3)
    degree=models.CharField(max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    sex=models.CharField(max_length=10)

