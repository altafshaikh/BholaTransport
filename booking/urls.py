from django.conf.urls import url
from . import views

app_name = 'booking'

urlpatterns = [
    url("", views.Booking, name="booking"),
    # url("booked/$", views.Booked, name="booked"),

]
