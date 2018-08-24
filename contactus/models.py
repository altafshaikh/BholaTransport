from django.db import models
from django.contrib import auth
from django.contrib.auth.models import Permission, User


class Contact(models.Model):
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    email =  models.EmailField(max_length = 2500)
    phone =  models.CharField(max_length = 100)
    subject= models.CharField(max_length = 250)
    message= models.CharField(max_length = 10000)

    def __str__(self):
        return str(self.first_name+" " + self.last_name)
