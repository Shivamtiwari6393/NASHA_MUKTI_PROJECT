from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


# REGISTRATION FORM----------REGISTRATION FORM----------------------REGISTRATION FORM-------------------REGISTRATION FORM----------REGISTRATION FORM------------


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:

        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


# LOGIN-IN FORM---------LOGIN-IN FORM--------------LOGIN-IN FORM------------LOGIN-IN FORM------------LOGIN-IN FORM-----------------------


# PATIENT FORM------PATIENT FORM------------PATIENT FORM-----------PATIENT FORM-----------PATIENT FORM--------PATIENT FORM----------PATIENT FORM-------PATIENT FORM-


class patientform(forms.Form):
    name = forms.CharField(label='Full Name', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Patient Name'}))
    age = forms.IntegerField(label='Age', min_value=0)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
    )
    contact_number = forms.CharField(
        label='Contact Number', min_length=10, max_length=10)
    pin_code = forms.CharField(label='Pin Code', max_length=6)
    address = forms.CharField(label='Address', max_length=50)
    state = forms.CharField(label='State', max_length=15)
    district = forms.CharField(label='District', max_length=15)
    addiction = forms.CharField(label='Addiction', max_length=15)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
