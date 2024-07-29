from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['default_phone_number', 'default_postcode', 'default_town_or_city', 'default_street_address1', 'default_street_address2']
        widgets = {
            'default_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'default_postcode': forms.TextInput(attrs={'class': 'form-control'}),
            'default_town_or_city': forms.TextInput(attrs={'class': 'form-control'}),
            'default_street_address1': forms.TextInput(attrs={'class': 'form-control'}),
            'default_street_address2': forms.TextInput(attrs={'class': 'form-control'}),
        }

