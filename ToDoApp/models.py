from django.db import models
from datetime import datetime

# Create your models here.

class Tasks(models.Model):
    name = models.CharField(max_length=100, unique=True)
    importance = models.CharField(max_length=100)
    description = models.TextField()
    TaskMade = models.DateTimeField(default=datetime.now())
    TaskDue = models.CharField(max_length=100)