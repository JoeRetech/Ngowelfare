from django import forms
from .models import Volunteer

class EmailForm(forms.Form):
    volunteer = forms.ModelChoiceField(
        queryset=Volunteer.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )
