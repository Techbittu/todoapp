from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegisterForm



class SignupView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(password=raw_password, email=email)
            email_subject = f"Witaj {user.username}!"
            email_message = "Aktywuj swoje konto!"
            send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, [user.email])
            login(request, user)
            return redirect('home')
        return render(request, 'signup.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class LogoutView(View):
    def get(self, request):
        return render(request, 'home.html')


class HomeView(TemplateView):
    template_name = 'home.html'


class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')


