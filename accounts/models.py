from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from phonenumber_field.modelfields import PhoneNumberField


class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone, password=None, **other_fields):
        if not email:
            return ValueError("User must have an email address!")
        if not username:
            return ValueError("User must have a username!")
        if not first_name:
            return ValueError("User must have a first name!")
        if not last_name:
            return ValueError("User must have a last name!")
        if not phone:
            return ValueError("User must have a phone number!")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            **other_fields
        )
        # hashed_password = make_password(password)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, last_name, phone, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(null=False, blank=False, max_length=50, unique=True)
    first_name = models.CharField(null=False, blank=False, max_length=50)
    last_name = models.CharField(null=False, blank=False, max_length=50)
    email = models.EmailField(null=False, blank=False, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    phone = PhoneNumberField(unique=True, null=False, blank=False, max_length=13)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'phone']

    objects = UserAccountManager()

    def __str__(self):
        return str(self.username)

class UserAddress(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()

    REQUIRED_FIELDS = ['address', 'city', 'zipcode']

    def __str__(self):
        return self.user.name + ' Address'




