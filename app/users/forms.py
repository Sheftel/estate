from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.forms import ModelForm

from users.models import Client

User = get_user_model()
# Sign Up Form


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=False, help_text='Optional')
    phone = forms.CharField(validators=[
            RegexValidator(
                regex=r'^\+?1?\d{8,15}$',
                message="Phone number format: '+999999999'. Up to 15 digits allowed."
            )])
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'name',
            'phone',
            'email',
            'password1',
            'password2',
            ]


class QuestionsForm(ModelForm):
    class Meta:
        model = Client
        fields = ['age', 'sex', 'partner', 'kids']
