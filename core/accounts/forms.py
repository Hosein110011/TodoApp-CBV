from django import forms
from .models import User



class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password','password1']


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=255, required=True)
    
    