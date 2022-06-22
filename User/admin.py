from django.contrib import admin
from .models import Country, Source, Person

admin.site.register(Country)
admin.site.register(Source)
admin.site.register(Person)