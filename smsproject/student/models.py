from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    course = models.CharField(max_length=100)
    address = models.TextField()



    def __str__(self):
        return f"{self.full_name}"
