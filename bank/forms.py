from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Client, Employee


class EmployeeForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['password', ]


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['password', ]
