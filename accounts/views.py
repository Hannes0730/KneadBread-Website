from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm


# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            print(user)
            if user:
                login(request, user)
                return redirect('/')

        context = {
            'login_form': form,
        }
        return render(request, "login.html", context=context)

@login_required(login_url='loginuser')
def logoutUser(request):
    if request.user:
        logout(request)
        messages.success(request, "Thank You for Using KneadBread!")
        return redirect('loginuser')


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        user_form = RegisterForm(request.POST or None)
        print("Form Registration")
        if user_form.is_valid():
            user_form.save()

            email = user_form.cleaned_data.get('email')
            password = user_form.cleaned_data.get('password2')

            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')

        context = {
            'register_form': user_form
        }
        return render(request, "register.html", context=context)
