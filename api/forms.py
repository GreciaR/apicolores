from django import forms
from .models import Color
from django.utils.translation import ugettext_lazy as _

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields= ['name', 'hexadecimal', 'red', 'green', 'blue']