from django import forms
from collector.models import Viewer

class FormClass(forms.ModelForm):
    survey_age = forms.FloatField(error_messages={'required':'Please enter your age'})
    survey_gender = forms.CharField(error_messages={'required':'Please enter your gender'})

    class Meta:
        model = Viewer
        fields = ('survey_age', 'survey_age',)