from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .forms import patientform
from .models import Patient
from django.contrib import messages


# REGISTRATION VIEW---------REGISTRATION VIEW----------REGISTRATION VIEW---------REGISTRATION VIEW-----------REGISTRATION VIEW-------------REGISTRATION VIEW---


def register(request):
    print("entererd")
    if request.method == 'POST':
        print('inside post')
        form = RegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            print('user : ', user)

            # Automatically log the user in after registration
            email = form.cleaned_data['email']
            print('email :', email)
            password = form.cleaned_data['password1']
            print('password : ', password)
            user = authenticate(request, email=email, password=password)
            print('auth user ', user)
            print(user)
            if user:
                print('before login', user)
                login(request, user)
                print('logged in', user)
                messages.success(request, 'Registration successful')
                print('redirected')
                return redirect('/patient')
            else:
                messages.error(request, 'Authentication failed')
        else:

            messages.error(request, 'Form is invalid')
    else:
        print('initialized')
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


# LOGIN VIEW-----LOGIN VIEW--------LOGIN VIEW---------LOGIN VIEW--------------LOGIN VIEW-----------------------LOGIN VIEW-----------LOGIN VIEW--------------LOGIN VIEW-----------


def user_login(request):
    print('ENTERED')
    if request.method == 'POST':
        print('INSIDE POST', request)
        email = request.POST['email']
        print('EMAIL', email)
        password = request.POST['password']
        print('password', password)
        user = authenticate(request, email=email, password=password)
        print('user', user)
        if user is not None:
            login(request, user)

            return redirect('/patient')
        else:

            messages.error(
                request, 'Authentication failed. Please check your credentials.')
    return render(request, 'login.html')


def user_logout(request):
    print("logged out")
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
                contact_number=formp.cleaned_data['contact_number'],
                address=formp.cleaned_data['address'],
                state=formp.cleaned_data['state'],
                district=formp.cleaned_data['district'],
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
