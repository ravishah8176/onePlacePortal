import email
from queue import Empty
from django.db import models

# Create your models here.
class studentDetails(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50,  blank=False)
    rollNo = models.CharField(max_length=15,  blank=False)
    gender = models.CharField(max_length=10, blank=False)
    phoneNumber = models.IntegerField(blank=False)
    
    def __str(self):
        return self.name
