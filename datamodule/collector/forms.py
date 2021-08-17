from django import forms
from django.db import models
from django.db.models import fields
from collector.models import Viewer
from collector.models import Tags

class FormClass(forms.ModelForm):
    survey_age = forms.FloatField(error_messages={'required':'Please enter your age'})
    survey_gender = forms.CharField(error_messages={'required':'Please enter your gender'})
    survey_name = forms.CharField(error_messages={'required':'Please enter your name'})
    

    class Meta:
        model = Viewer
        fields = ('survey_age', 'survey_age','survey_name')

    class Meta:
        model=Tags
        fields=('timestamp','emotion')