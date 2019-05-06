from django import forms
from .models import *
class RegisterForm(forms.ModelForm):
    registerinfo_id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    class Meta:
        model = RegisterInfo
        exclude = ['status']
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
            'user_email': forms.EmailInput(attrs={'readonly': 'readonly'}),
        }
class RunnerForm(forms.ModelForm):

     class Meta:
        model = Runner
        fields = '__all__'


class ManagerForm(forms.ModelForm):
     class Meta:
        model = Manager
        fields = '__all__'


class Teamform(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class SoloRunnerform(forms.ModelForm):
    class Meta:
        model = SoloRunner
        exclude = ['runner_bib']

class Driverform(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = ['team_id']
