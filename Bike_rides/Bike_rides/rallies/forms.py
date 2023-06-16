from django import forms
from django.forms import ModelChoiceField
from .models import Rally, ParticipantsList

from datetime import datetime


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.description


class RallyRegisterForm(forms.ModelForm):

    class Meta:
        model = ParticipantsList
        exclude = ['id_participant']

    id_rally = MyModelChoiceField(queryset=Rally.objects.filter(date__gt=datetime.today()), label='Rally')


    # description = ModelChoiceField(queryset=Rally.objects.values_list('description'), label='Rally')
    # name = forms.CharField(label='Name', max_length=30, help_text='Fill with your first name')
    # name = forms.CharField(label='Name')
    # birth_date = forms.DateField(label='Birth date', widget=forms.SelectDateWidget(years=range(1980, 2024)))
    # email = forms.EmailField(label='E-mail', initial='mail@domena.pl', required=False)
    # post_code = forms.RegexField(label='Postal code', regex='^\d{2}-\d{3}$')

# Upload files
# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()