from django.db import models

# Create your models here.

class Viewer(models.Model):
    survey_age = models.FloatField(null=True, blank=True)
    survey_gender = models.CharField(max_length=15, null=True, blank=True)