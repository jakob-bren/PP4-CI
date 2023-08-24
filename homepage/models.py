from django.db import models

# Create your models here.

class Student(models.Model):
  name = models.CharField(max_length=250)
  rollno = models.CharField(max_length=250)
  
  def __str__(self):
    return self.name

class Menu(models.Model):
  title = models.CharField(max_length=90, unique=True)
  price = models.FloatField()
  desc = models.CharField(max_length=520, default='No description added yet.')
  ingredients = models.CharField(max_length=260)
  
  def __str__(self):
    return self.title
  
  


  