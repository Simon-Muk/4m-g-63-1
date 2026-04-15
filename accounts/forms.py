from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from captcha.fields import CaptchaField


class RegisterForm(UserCreationForm):

    class Meta:

        model = CustomUser

        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'phone',
            'age',
            'city',
            'address',
            'birth_date',
            'gender',
            'avatar',
            'bio',
            'hobby',
            'education'
        ]

from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):

    captcha = CaptchaField()        




