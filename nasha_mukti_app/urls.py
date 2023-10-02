
from django.urls import path
from nasha_mukti_app import views
urlpatterns = [
    path("", views.register, name="register"),
    path('login/', views.user_login, name='login'),
    path('logout', views.user_logout, name="logout"),
    path("patient", views.create_patient, name="patient_details"),
    path('fetch', views.fetch, name='fetch'),
]
