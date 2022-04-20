from django import forms

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
    date = forms.DateField(widget=DatePickerDateInput)
    time = forms.TimeField(widget=TimePickerTimeInput)
    poo = forms.BooleanField()

    class Meta:
        model = Event
        fields = "__all__"
