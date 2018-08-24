from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Contact
from .forms import ContactForm



def ContactUs(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact = form.save(commit=False)
        user=request.user
        contact.first_name = form.cleaned_data.get('first_name')
        contact.last_name = form.cleaned_data.get('last_name')
        contact.email = form.cleaned_data.get('email')
        contact.phone = form.cleaned_data.get('phone')
        contact.subject = form.cleaned_data.get('subject')
        contact.message = form.cleaned_data.get('message')
        contact.save()
        return render(request, 'thanks1.html', {'contact': contact,'user':user})
    context = {
            "form": form,
        }
    return render(request, 'contactus.html', context)
