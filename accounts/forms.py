from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount, UserAddress


class LoginForm(forms.Form):
    email = forms.EmailField(widget=TextInput(
        attrs={
            "class": "form-control",
            "id": "inputEmail",
            "placeholder": "Email",
        }))
    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class": "form-control",
                "id": "inputPassword",
                "placeholder": "Password",
            }
        )
    )

    def clean(self):
        print("cleaning")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        email_filter = UserAccount.objects.filter(email__iexact=email)
        print(email_filter)
        if not email_filter.exists():
            self.add_error('email', "Invalid Credentials!")
        else:
            if email and password:
                user = authenticate(email=email, password=password)
                if not user:
                    self.add_error('password', "Invalid Credentials!")
        return self.cleaned_data


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(
        attrs={
            "class": "form-control",
            "id": "username",
            # "placeholder": "Username",
        }))
    first_name = forms.CharField(widget=TextInput(
        attrs={
            "class": "form-control",
            "id": "inputFirstName",
            # "placeholder": "First Name",
        }))
    last_name = forms.CharField(widget=TextInput(
        attrs={
            "class": "form-control",
            "id": "inputLastName",
            # "placeholder": "Last Name",
        }))
    phone = forms.CharField(widget=TextInput(
        attrs={
            "class": "form-control",
            "id": "inputPhoneNumber",
            "placeholder": "+639123456789",
        }))
    email = forms.EmailField(widget=TextInput(
        attrs={
            "class": "form-control",
            "id": "inputEmail",
            # "placeholder": "Email",
        }))
    password1 = forms.CharField(label='Password',
                                widget=PasswordInput(
                                    attrs={
                                        "class": "form-control",
                                        "id": "password1",
                                        # "placeholder": "Password",

                                    }
                                )
                                )
    password2 = forms.CharField(label="Password Confirmation",
                                widget=PasswordInput(
                                    attrs={
                                        "class": "form-control",
                                        "id": "password2",
                                        # "placeholder": "Confirm Password",
                                    }
                                )
                                )

    class Meta:
        model = UserAccount
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')

    def clean_firstname(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name[0].upper() + first_name[1:].lower()

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        return last_name[0].upper() + last_name[1:].lower()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_filter = UserAccount.objects.filter(email__iexact=email)
        if email_filter.exists():
            self.add_error('email', "Email is already registered!")
        return email.lower()

    def clean_username(self):
        username = self.cleaned_data.get("username")
        username_filter = UserAccount.objects.filter(username__iexact=username)
        if username_filter.exists():
            self.add_error('username', "Username is already taken")
        return self.cleaned_data['username']


class Address(forms.ModelForm):
    address = forms.CharField(widget=TextInput(
        attrs={
            "class": "form-control",
            "id": "address",
        }))
    city = forms.CharField(widget=TextInput(
        attrs={
            "class": "form-control",
            "id": "city",
        }))
    zipcode = forms.IntegerField(widget=TextInput(
        attrs={
            "class": "form-control",
            "id": "zipcode",
        }))

    class Meta:
        model = UserAddress
        fields = ('address', 'city', 'zipcode')
