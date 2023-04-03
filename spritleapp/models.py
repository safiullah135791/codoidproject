from django.db import models

# Create your models here.
class Data(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField(max_length=25)
    Password1 = models.CharField(max_length=16)

class Equation(models.Model):
    Multiple = models.IntegerField()
    Plus = models.IntegerField()
    Minus = models.IntegerField()
    Divide = models.IntegerField()
