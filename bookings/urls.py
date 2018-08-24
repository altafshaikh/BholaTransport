from django.conf.urls import url
from django.contrib import admin
from . import views


app_name="bookings"

urlpatterns = [
  # url(r'^(?P<pk>[0-9]+)/$',views.DetailView .as_view(),name ='book_detail'),
  url('',views.DetailView .as_view(),name ='book_detail'),
]
