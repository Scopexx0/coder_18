from django.db import models

# Create your models here.
class Member(models.Model):

    nombre=models.CharField(max_length=40)
    dni = models.IntegerField()
    born_date = models.DateField()
