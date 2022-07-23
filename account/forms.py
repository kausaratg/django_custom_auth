from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django.contrib.auth import authenticate, login, logout

class UserRegistration(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['email', 'company_name', 'phone_number', 'password1', 'password2']




class UserLogin(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')

            if not authenticate(email= email, password=password):
                raise forms.ValidationError('Invalid credentials')


