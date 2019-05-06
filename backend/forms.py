from django import forms
from .models import *
class RegisterForm(forms.ModelForm):
     class Meta:
        model = RegisterInfo
        fields = '__all__'

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
        fields = '__all__'

class Driverform(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = ['team_id']
