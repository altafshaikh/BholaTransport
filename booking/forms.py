from django import forms
from .models import Booking


class BookForm(forms.ModelForm):


    class Meta:
        model = Booking
        fields = ['source', 'destination', 'material', 'truck_type','date']
        #
        # widgets = {
        #     'source': forms.TextInput(attrs={'placeholder': 'enter source'}),
        #     'destination': forms.TextInput(attrs={'placeholder': 'enter destination'}),
        #     'material': forms.TextInput(attrs={'placeholder': 'material'}),
        #     'truck_type':forms.TextInput(attrs={'placeholder': 'truck type'}),
        #     'date': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        #     }
