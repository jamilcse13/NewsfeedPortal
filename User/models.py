from django.db import models
from multiselectfield import MultiSelectField
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
    country = MultiSelectField(choices=COUNTRY_CHOICES)
    source = MultiSelectField(choices=SOURCE_CHOICES)
    keyword = models.CharField(max_length=50, null=True)