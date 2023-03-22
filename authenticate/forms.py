from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email')
        # fields = ('first_name', 'last_name', 'username', 'email')


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
