from django import forms

from catalog.models import Person


class TriangleForm(forms.Form):
    leg_1 = forms.IntegerField(label='input 1st leg of triangle', required=False)
    leg_2 = forms.IntegerField(label='input 2nd leg of triangle', required=False)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
