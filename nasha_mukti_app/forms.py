from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


# REGISTRATION FORM----------REGISTRATION FORM----------------------REGISTRATION FORM-------------------REGISTRATION FORM----------REGISTRATION FORM------------

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your CustomUser model


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Email'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Last Name'}))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        help_text='',  # Clear the help text as you did in your code
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
