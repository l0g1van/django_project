from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from catalog.models import Person


class TriangleForm(forms.Form):
    leg_1 = forms.IntegerField(label='input 1st leg of triangle', required=False)
    leg_2 = forms.IntegerField(label='input 2nd leg of triangle', required=False)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']


class EmailForm(forms.Form):
    email = forms.EmailField(label="Email Address", initial='test@example.com')
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )
    date_time = forms.DateTimeField(label='Time when you want to get the message',
                                    input_formats=['%Y-%m-%d %H:%M:%S'], initial=timezone.now())

    def clean_date_time(self):
        date_time = self.cleaned_data['date_time']
        if date_time < timezone.now():
            raise ValidationError('Time field cannot be earlier then current')
        elif date_time > timezone.now() + timezone.timedelta(days=2):
            raise ValidationError('Time field cannot be older then 2 days')
        else:
            return date_time
