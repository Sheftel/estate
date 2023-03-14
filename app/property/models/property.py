from django.db.models import Model, CharField, IntegerField, DecimalField, TextField, ForeignKey, CASCADE
from django.core.validators import RegexValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


class Property(Model):
    owner = ForeignKey('Owner', on_delete=CASCADE, null=False, related_name="properties")

    # TODO: add validators to numerical values
    type = CharField(
        choices=[
            ('residential', _('Residential')),
            ('commercial', _('Commercial'))
        ],
        max_length=15)
    category = CharField(
        choices=[
            ('flat', _('Flat')),
            ('house', _('House')),
            ('apartments', _('Apartments'))
        ],
        max_length=15)
    area = DecimalField(max_digits=7, decimal_places=3)
    room_count = IntegerField(default=1)
    floor = IntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ])
    address = CharField(max_length=255)
    deal = CharField(
        choices=[
            ('rent', _('Rent')),
            ('purchase', _('Purchase'))
        ],
        max_length=15)
    price = DecimalField(max_digits=8, decimal_places=0)
    description = TextField(blank=True)

    class Meta:
        verbose_name_plural = _('Properties')
