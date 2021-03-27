from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.contrib.auth import password_validation

polish_password_help_text = '''
</ul>
<li>Your password must not be similar to any other information.</li>
<li>Your password must be at least 8 characters long.</li>
<li>Your password cannot be too common.</li>
<li>Your password cannot consist entirely of numbers.</li>
</ul>
'''

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email Address")
    username = forms.CharField(max_length=255, required=True, label="Username")
    password1 = forms.CharField(
    label="Password",
    strip=False,
    widget=forms.PasswordInput,
    help_text=polish_password_help_text,
    )
    password2 = forms.CharField(
    label="confirm Password",
    strip=False,
    widget=forms.PasswordInput,
    help_text="Enter Same Password Again."
    )
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]