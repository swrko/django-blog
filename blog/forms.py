from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError, Form


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_repeat = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        if self.cleaned_data.get('password') == self.cleaned_data.get('password_repeat'):
            return True
        raise ValidationError("Si kokot a hesla sa musia zhodovat")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class LoginUserForm(Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
