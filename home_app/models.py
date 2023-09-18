from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import Group, Permission


# MODEL FOR REGISTRATION-------------------------------------------------------------------------------------


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

    # Add your custom fields here
    # For example, you might add a profile picture field:
    # profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    # You can add more custom fields as needed

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        # Define a custom related_name for groups and user_permissions
        # This avoids the clash with the built-in User model
        # You can use any related_name you prefer
        permissions = [
            ("can_change_group", "Can change group"),
            ("can_change_permission", "Can change permission"),
        ]

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


# END REGISTRATION-------------------------------------------------------------------------------------------------------------------------


class Patient(models.Model):
    name = models.CharField(max_length=100, verbose_name='Full Name')
    age = models.IntegerField(verbose_name='Age')
    contact_number = models.CharField(
        max_length=15, verbose_name='Contact Number')
    address = models.CharField(max_length=50, verbose_name='Address')
    state = models.CharField(max_length=15, verbose_name='State')
    district = models.CharField(max_length=15, verbose_name='District')

    def __str__(self):
        return self.name
