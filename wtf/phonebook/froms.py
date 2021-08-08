from django import forms

from . import models


class CreatePersonForm(forms.ModelForm):
    phones = forms.CharField(widget=forms.Textarea(), help_text='separated by new line ')

    class Meta:
        model = models.Person
        fields = (
            'name',
            'phones'
        )
