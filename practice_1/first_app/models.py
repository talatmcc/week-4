from django.db import models
# from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class MyModel(models.Model):
    name = models.CharField(max_length=100, default='Unknown')
    roll = models.IntegerField(primary_key=True, default=0)
    father_name = models.CharField(max_length=100, default='Unknown')
    total_marks = models.IntegerField(default=0)
    # agree_disagree = models.BinaryField(default=b'\x01')  # Default as a byte
    nationality = models.CharField(max_length=255, default='Unknown')
    # birth_date = models.DateField(default=timezone.now)  # Default to current date
    # date_time_field = models.DateTimeField(default=timezone.now)  # Default to current datetime
    # class_time = models.DurationField(default=timedelta())  # Default to 0 duration
    # pdf = models.FileField(upload_to='files/', default='files/default.pdf')
    # picture = models.ImageField(upload_to='images/', default='images/default.jpg')
    # last_visited = models.TimeField(default=timezone.now().time())  # Default to current time

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(primary_key=True)        
    address = models.TextField()    
    father_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.roll} - {self.name} "





