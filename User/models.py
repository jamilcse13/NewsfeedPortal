from django.db import models
from django import forms
from django.contrib.auth.models import User


class Setting(models.Model):
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


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = forms.MultipleChoiceField(choices=COUNTRY_CHOICES, widget=forms.CheckboxSelectMultiple)
    source = forms.MultipleChoiceField(choices=SOURCE_CHOICES, widget=forms.CheckboxSelectMultiple)
    keyword = models.CharField(max_length=50, null=True)