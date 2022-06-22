from django.db import models
from django import forms
from django.contrib.auth.models import User


class Setting(models.Model):
    country = models.CharField(max_length=10)
    source = models.CharField(max_length=40)

    def __str__(self):
        return self.country

class Country(models.Model):
    key = models.CharField(max_length=10)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Source(models.Model):
    key = models.CharField(max_length=10)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, blank=True, null=True)
    keyword = models.CharField(max_length=124)

    def __str__(self):
        return self.name








# class Setting(models.Model):
#     COUNTRY_CHOICES = (
#         ('au', 'Australia'),
#         ('ca', 'Canada'),
#         ('cn', 'China'),
#         ('eg', 'Egypt'),
#         ('fr', 'France'),
#         ('in', 'India'),
#         ('it', 'Italy'),
#         ('mx', 'Mexico'),
#         ('nz', 'New Zealand'),
#         ('ru', 'Russia'),
#         ('uk', 'UK'),
#         ('us', 'USA')
#     )

#     SOURCE_CHOICES = (
#         ('bbc-news', 'BBC'),
#         ('abc-news', 'ABC'),
#         ('al-jazeera-english', 'AL-Jazeera'),
#         ('marca', 'Marca'),
#         ('cnn', 'CNN'),
#         ('reuters', 'Reuters')
#     )
