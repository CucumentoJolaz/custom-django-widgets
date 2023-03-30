from django import forms
from django.forms import CheckboxSelectMultiple

from .models import Event, EventsBunch
from .widgets import XDSoftDateTimePickerInput, BootstrapDateTimePickerInput, FengyuanChenDatePickerInput, \
    CheckboxSelectMultipleWithLinksInput


class DateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'date')

    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )


class XDSoftEventForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=XDSoftDateTimePickerInput())

    class Meta:
        model = Event
        fields = ('name', 'date')


class BootstrapEventForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=BootstrapDateTimePickerInput())

    class Meta:
        model = Event
        fields = ('name', 'date')


class FengyuanChenEventForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%d/%m/%Y'], widget=FengyuanChenDatePickerInput())

    class Meta:
        model = Event
        fields = ('name', 'date')


class EventsSelectionForm(forms.ModelForm):
    queryset = Event.objects.all()
    events = forms.ModelMultipleChoiceField(queryset=queryset,
                                            widget=CheckboxSelectMultipleWithLinksInput(queryset=queryset))

    class Meta:
        model = EventsBunch
        fields = ('name', 'events')
