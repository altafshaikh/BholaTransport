from django.db import models
from django.contrib import auth
from django.utils import timezone
import datetime
from django.contrib.auth.models import Permission, User


MATERIAL_CHOICE=(
('Cement','Cement'),
('House Hold Goods','House Hold Goods'),
('Building Materials','Building Materials'),
('Chemicals','Chemicals'),
('Coal And Ash','Coal And Ash'),
('Container','Container'),
('Cotton seed','Cotton seed'),
('Fertilizers','Fertilizers'),
('Fruits And Vegetables','Fruits And Vegetables'),
('Furniture And Wood Products','Furniture And Wood Products'),
('Industrial Equipments','Industrial Equipments'),
('Iron sheets or bars or scraps','Iron sheets or bars or scraps'),
('Medicals','Medicals'),
('Metals','Metals'),
('Mill Jute Oil','Mill Jute Oil'),
('Others','Others'),
('Packed Food','Packed Food'),
('Plastic Pipes or other products','Plastic Pipes or other products'),
)

TRUCK_TYPE=(
('loader','Loader'),
('truck','Truck'),
)


class Booking(models.Model):
    user = models.ForeignKey(User,default = 1,on_delete = models.CASCADE)
    source = models.CharField(max_length = 250)
    destination = models.CharField(max_length = 250)
    material = models.CharField(max_length=50, choices=MATERIAL_CHOICE, default='black')
    truck_type= models.CharField(max_length=50, choices=TRUCK_TYPE, default='black')
    date= models.DateField()

    def __str__(self):
        return str(self.user.username)
