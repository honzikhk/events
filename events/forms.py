from django import forms
import datetime

from events.models import Event


class DatePickerDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'date'}})
        super(DatePickerDateInput, self).__init__(*args, **kwargs)


class TimePickerTimeInput(forms.TimeInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'time'}})
        super(TimePickerTimeInput, self).__init__(*args, **kwargs)


class EventForm(forms.ModelForm):
    date = forms.DateField(widget=DatePickerDateInput, initial=datetime.date.today)
    time = forms.TimeField(widget=TimePickerTimeInput, initial=datetime.datetime.now)
    note = forms.CharField(required=False)
    #poo = forms.BooleanField(required=False)

    class Meta:
        model = Event
        fields = "__all__"
