from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import *


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "login__element",
                "name": "username",
                "id": "username-field",
                "placeholder": "Имя пользователя",
            }
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "login__element",
                "name": "password",
                "id": "password-field",
                "placeholder": "Пароль",
            }
        ),
    )


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "login__element",
                "name": "username",
                "id": "username2-field",
                "placeholder": "Имя пользователя",
            }
        ),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "login__element",
                "type": "password",
                "name": "password",
                "id": "password2-field",
                "placeholder": "Пароль",
            }
        ),
    )
    password2 = forms.CharField(
        label="Повтор пароля",
        widget=forms.PasswordInput(
            attrs={
                "class": "login__element",
                "type": "password",
                "name": "password",
                "id": "repeat_password-field",
                "placeholder": "Повторите пароль",
            }
        ),
    )
