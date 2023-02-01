from django import forms


class TriangleForm(forms.Form):
    leg_1 = forms.IntegerField(label='input 1st leg of triangle', required=False)
    leg_2 = forms.IntegerField(label='input 2nd leg of triangle', required=False)

