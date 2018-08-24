# from django.views.generic import CreateView, TemplateView
# from django.urls import reverse_lazy
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Booking
from .forms import BookForm



def Booking(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        book = form.save(commit=False)
        user = request.user
        book.user=user
        book.source = form.cleaned_data.get('source')
        book.destination = form.cleaned_data.get('destination')
        book.material = form.cleaned_data.get('material')
        book.truck_type = form.cleaned_data.get('truck_type')
        book.date = form.cleaned_data.get('date')

        book.save()
        return render(request, 'thanks0.html', {'book': book,'user':user})
    context = {
            "form": form,
        }
    return render(request, 'booking.html', context)

def Booked(request):
    return render(request, 'thanks0.html')
