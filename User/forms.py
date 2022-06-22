from django import forms
from django.core import validators
from django.contrib.auth.models import User

from .models import Person

COUNTRY_CHOICES = (
    ('au', 'Australia'),
    ('ca', 'Canada'),
    ('cn', 'China'),
    ('eg', 'Egypt'),
    ('fr', 'France'),
    ('in', 'India'),
    ('it', 'Italy'),
    ('mx', 'Mexico'),
    ('nz', 'New Zealand'),
    ('ru', 'Russia'),
    ('uk', 'UK'),
    ('us', 'USA')
)

SOURCE_CHOICES = (
    ('bbc-news', 'BBC'),
    ('abc-news', 'ABC'),
    ('al-jazeera-english', 'AL-Jazeera'),
    ('marca', 'Marca'),
    ('cnn', 'CNN'),
    ('reuters', 'Reuters')
)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    fname = forms.CharField(max_length=50)
    lname = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    pass1 = forms.CharField(widget = forms.PasswordInput, validators = [validators.MinLengthValidator(6)])
    pass2 = forms.CharField(widget = forms.PasswordInput, validators = [validators.MinLengthValidator(6)])

class SettingForm(forms.Form):
    country = forms.MultipleChoiceField(choices=COUNTRY_CHOICES)
    source = forms.MultipleChoiceField(choices=SOURCE_CHOICES)


class PersonCreationForm(forms.Form):
    class Meta:
        model = Person
        fields = ('name', 'country', 'source')