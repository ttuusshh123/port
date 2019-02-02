from django import forms
from .models import Port


class PortForm(forms.ModelForm):
    class Meta:
        model = Port
        fields = '__all__'
