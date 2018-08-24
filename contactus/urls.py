from django.conf.urls import url
from django.contrib import admin
from . import views


app_name="contactus"

urlpatterns = [


  url("",views.ContactUs, name="contactus"),
]
