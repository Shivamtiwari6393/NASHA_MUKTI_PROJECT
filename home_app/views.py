from .forms import CustomLoginForm  # Import your custom login form
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login, logout
# from .forms import CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .forms import patientform
from .models import Patient
from django.http import HttpResponseRedirect
from django.urls import reverse

# REGISTRATION VIEW---------REGISTRATION VIEW----------REGISTRATION VIEW---------REGISTRATION VIEW-----------REGISTRATION VIEW-------------REGISTRATION VIEW---


# def register(request):
#     if request.method == 'POST':as
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect to login page on successful registration
#             # Use '/' as the default redirect URL
#             redirect_url = request.META.get('HTTP_REFERER', '/')
#             return redirect(redirect_url)
#     else:
#         form = RegistrationForm()
#     return render(request, 'register.html', {'form': form})


# from .forms import CustomAuthenticationForm


from django.contrib import messages


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


# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         print(form)
#         if form.is_valid():
#             user = form.save()
#             print(user, '1')
#             # Automatically log the user in after registration
#             email = form.cleaned_data['email']
#             print(email, '2')
#             password = form.cleaned_data['password1']
#             print(password)
#             user = authenticate(request, email=email, password=password)
#             print(user, '3')
#             if user:

#                 login(request, user)
#                 # Redirect to user's profile page after registration
#                 # redirect_url = request.META.get('HTTP_REFERER', '/')
#                 return HttpResponseRedirect(reverse(''))
#     else:
#         form = RegistrationForm()
#         print(form, '4')
#     return render(request, 'register.html', {'form': form})


# def user_login(request):
#     if request.method == 'POST':
#         form = CustomLoginForm(request, data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)

#             if user:
#                 login(request, user)
#                 # Redirect to a success page (e.g., user's profile)
#                 return redirect('profile')  # Update to your desired URL
#     else:
#         form = CustomLoginForm(request)

#     return render(request, 'login.html', {'form': form})


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
            # Redirect to a protected page for authenticated users
            return redirect('/patient')
        else:
            # Authentication failed, display an error message
            messages.error(
                request, 'Authentication failed. Please check your credentials.')
    return render(request, 'login.html')


def user_logout(request):
    print("logged out")
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


# ---LOGIN VIEW----------------------------------------------------------------------


# @login_required
# def protected_view(request):
#     return render(request, 'protected.html')


# class CustomLoginView(LoginView):
#     authentication_form = CustomAuthenticationForm
#     template_name = 'login.html'


# def custom_logout(request):
#     logout(request)
#     return redirect('login')


# PATIENT DETAILS VIEW ---------------------PATIENT DETAILS VIEW--------------------PATIENT DETAILS VIEW---------------PATIENT DETAILS VIEW-------------------


# def patient_details_view(request):
#     if request.method == 'POST':
#         formp = patientform(request.POST)
#         if formp.is_valid():
#             # Process form data (e.g., save patient details) here
#             return redirect('success')  # Redirect to a success page
#     else:
#         formp = patientform()
#     return render(request, 'patient.html', {'patient_forms': formp})


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
