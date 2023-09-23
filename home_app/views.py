from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .forms import patientform
from .models import Patient
from django.contrib import messages


# REGISTRATION VIEW----------REGISTRATION_VIEW----------REGISTRATION_VIEW----------REGISTRATION_VIEW----------REGISTRATION_VIEW----------REGISTRATION_VIEW


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log the user in after registration
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Registration successful')
                return redirect('/patient')
            else:
                messages.error(request, 'Authentication failed')
        else:

            messages.error(request, 'Form is invalid')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


# LOGIN VIEW----------LOGIN VIEW----------LOGIN VIEW----------LOGIN VIEW----------LOGIN VIEW----------LOGIN VIEW----------LOGIN VIEW----------LOGIN VIEW


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/patient')
        else:
            messages.error(
                request, 'Authentication failed. Please check your credentials.')
    return render(request, 'login.html')


# LOGOUT_VIEW----------LOGOUT_VIEW----------LOGOUT_VIEW----------LOGOUT_VIEW----------LOGOUT_VIEW----------LOGOUT_VIEW----------LOGOUT_VIEW----------LOGOUT_VIEW3


def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


# PATIENT VIEW-----------------PATIENT VIEW---------------------PATIENT VIEW----------------PATIENT VIEW--------------------PATIENT VIEW----------PATIENT VIEW-


def create_patient(request):
    if request.method == 'POST':
        formp = patientform(request.POST)
        if formp.is_valid():
            # Create a new patient object and save it to the database
            patient = Patient(
                name=formp.cleaned_data['name'],
                age=formp.cleaned_data['age'],
                gender=formp.cleaned_data['gender'],
                contact_number=formp.cleaned_data['contact_number'],
                pin_code=formp.cleaned_data['pin_code'],
                address=formp.cleaned_data['address'],
                state=formp.cleaned_data['state'],
                district=formp.cleaned_data['district'],
                addiction=formp.cleaned_data['addiction'],
            )
            patient.save()
            # Redirect to a success page or another view
            return redirect('/patient')
        else:
            # Handle form validation errors, you can display them in the template
            errors = formp.errors
            return render(request, 'patient.html', {'formp': formp, 'errors': errors})
    else:
        formp = patientform()
    return render(request, 'patient.html', {'formp': formp})
