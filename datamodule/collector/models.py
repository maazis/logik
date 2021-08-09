from django.db import models

# Create your models here.

class Viewer(models.Model):
    survey_age = models.FloatField(null=False, blank=False)
    survey_gender = models.CharField(max_length=15, null=False, blank=False)
    survey_name=models.CharField(max_length=50,null=False, blank=True )