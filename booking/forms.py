from django import forms
from django.forms import ModelForm
from .models import Offer
from .models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'phone']


class DateInput(forms.DateInput):
    input_type = 'date'


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = fields = '__all__'
        widgets = {
            'expiration_date': DateInput(),
        }
