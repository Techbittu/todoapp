from django import forms
from .models import Activity
from django.contrib.admin.widgets import AdminDateWidget
from bootstrap_datepicker_plus import DateTimePickerInput

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = [
            'activity',
            'project',
            'to_do_date',
            'end_date',
        ]
        labels = {
            'activity': 'Activity',
            'project':'Select Project',
            'to_do_date': 'start date and time',
            'end_date':'End_date and time',
        }
        help_texts = {
            'activity': 'Provide a name for the activity to be done.',
            'project':'Select the Project',
            'to_do_date': 'Enter the date of start in the appropriate format, e.g. 2020-02-25 18:00',
            'end_date':'Enter the Date of End'
            
        }
        widgets = {
            'to_do_date': DateTimePickerInput(format='%Y-%m-%d %H:%M'),
            'end_date': DateTimePickerInput(format='%Y-%m-%d %H:%M'),
        }


class RawActivityForm(forms.Form):
    activity   = forms.CharField(max_length=50)
    project = forms.CharField(max_length=50)
    to_do_date  = forms.DateTimeField()
    end_date = forms.DateTimeField()