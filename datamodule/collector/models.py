from django.db import models

# Create your models here.

class Viewer(models.Model):
    survey_age = models.FloatField()
    survey_gender = models.CharField(max_length=15)