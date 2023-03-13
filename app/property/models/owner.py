from django.db.models import Model, CharField, EmailField
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class Owner(Model):
    name = CharField(max_length=75)
    phone = CharField(
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{8,15}$',
                message="Phone number format: '+999999999'. Up to 15 digits allowed."
            )],
        max_length=17, null=True, blank=True)
    email = EmailField(blank=False, max_length=255, unique=True)
    type = CharField(
        choices=[
            ('AG', _('Agency')),
            ('PR', _('Private'))
        ],
        max_length=255)
