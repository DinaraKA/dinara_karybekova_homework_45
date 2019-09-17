from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Описание')
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Статус')
    details = forms.CharField(max_length=5000, required=True, label='Детали',
                              widget=widgets.Textarea)
    date = forms.DateField(required=True, input_formats=['%Y-%m-%d'], label='Дата выполнения')


