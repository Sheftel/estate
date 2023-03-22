from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models import Model, CharField, EmailField, IntegerField, BooleanField, OneToOneField, \
    CASCADE, PositiveIntegerField
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    name = CharField(blank=True, max_length=255)
    phone = CharField(
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{8,15}$',
                message="Phone number format: '+999999999'. Up to 15 digits allowed."
            )],
        max_length=17, null=True, blank=True)
    email = EmailField(blank=False, max_length=255, unique=True)

    username = None  # type: ignore
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']


class Client(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='client')

    # TODO: map choices or smth
    sex = BooleanField()
    # TODO: min value validator
    age = PositiveIntegerField(default=19)
    partner = BooleanField()
    # TODO: min value validator
    kids = PositiveIntegerField(default=0)
    type = CharField(
        choices=[
            ('company', _('Company')),
            ('private', _('Private'))
        ],
        max_length=255)
