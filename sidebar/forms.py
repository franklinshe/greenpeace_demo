from django import forms

# https://docs.djangoproject.com/en/3.1/topics/forms/

LABEL_CHOICES = (
    ("1", "Label 1"),
    ("2", "Label 2"),
    ("3", "Label 3"),
    ("4", "Label 4"),
    ("5", "Label 5"),
)

LOCATION_CHOICES = (
    ("1", "North America"),
    ("2", "South America"),
    ("3", "Africa"),
    ("4", "Europe"),
    ("5", "Asia"),
)

YEAR_CHOICES = (
    ("1", "2021"),
    ("2", "2020"),
    ("3", "2019"),
    ("4", "2018"),
    ("5", "2017"),
)

class ViewDataForm(forms.Form):
    label = forms.ChoiceField(choices = LABEL_CHOICES)
    location = forms.ChoiceField(choices = LOCATION_CHOICES)
    year = forms.ChoiceField(choices = YEAR_CHOICES)