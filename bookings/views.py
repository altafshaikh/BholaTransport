from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from booking.models import Booking
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView


class DetailView(DetailView):
	model=Booking
	template_name='detail.html'
