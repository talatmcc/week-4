from django import forms
import datetime
from django.forms.widgets import NumberInput
# from . models import Student  


class contactForm(forms.Form):
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    BIRTH_MONTH_CHOICES = ['January', 'February', 'March']
    BIRTH_DAY_CHOICES = ['1', '2', '3']

    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput()) 

    text = forms.CharField(widget=forms.Textarea)   
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    time = forms.TimeField()
    datetime = forms.DateTimeField()
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    # model_choice = forms.ModelChoiceField(
    #     queryset = MyModel.objects.all(),
    #     initial = 0
    #     )

