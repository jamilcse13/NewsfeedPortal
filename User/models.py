from django.db import models
from django.contrib.auth.models import User


class Setting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=10, null=True)
    source = models.CharField(max_length=50, null=True)
    keyword = models.CharField(max_length=50, null=True)