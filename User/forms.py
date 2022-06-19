from django import forms

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


class SettingForm(forms.Form):
    country_field = forms.MultipleChoiceField(choices=COUNTRY_CHOICES)
    source_field = forms.MultipleChoiceField(choices=SOURCE_CHOICES)