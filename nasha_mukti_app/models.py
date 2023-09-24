from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import Group, Permission


# REGISTRATION_MODEL-------------REGISTRATION_MODEL-------------REGISTRATION_MODEL-------------REGISTRATION_MODEL------------------REGISTRATION_MODEL----------------------


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        # Define a custom related_name for groups and user_permissions
        # This avoids the clash with the built-in User model
        # You can use any related_name you prefer

        def __str__(self):
            return self.email

    # Define related_name for groups and user_permissions to avoid clashes
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to.",
        related_name="customuser_set"  # Change 'customuser_set' to your preferred name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="customuser_set"  # Change 'customuser_set' to your preferred name
    )


# PATIENT_MODEL-----------PATIENT_MODEL----------------PATIENT_MODEL---------------------PATIENT_MODEL------------------PATIENT_MODEL-----------------PATIENT_MODEL--------------------------------------


class Patient(models.Model):
    name = models.CharField(max_length=100, verbose_name='Full Name')
    age = models.IntegerField(verbose_name='Age')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_number = models.CharField(
        max_length=15, verbose_name='Contact Number')
    pin_code = models.CharField(
        max_length=6, verbose_name='pin_code')
    address = models.CharField(max_length=50, verbose_name='Address')
    state = models.CharField(max_length=15, verbose_name='State')
    district = models.CharField(max_length=15, verbose_name='District')
    addiction = models.CharField(max_length=15, verbose_name='Addiction')

    def __str__(self):
        return self.name


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
