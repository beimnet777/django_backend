from django.db import models
class Analytics(models.Model):
  age_18_29=models.IntegerField(max_length=8)
  age_30_50=models.IntegerField(max_length=8)
  age_51=models.IntegerField(max_length=8)


# Create your models here.
