# Generated by Django 3.2.1 on 2023-03-15 08:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('phone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{8,15}$')])),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('type', models.CharField(choices=[('agency', 'Agency'), ('private', 'Private')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('residential', 'Residential'), ('commercial', 'Commercial')], max_length=15)),
                ('category', models.CharField(choices=[('flat', 'Flat'), ('house', 'House'), ('apartments', 'Apartments')], max_length=15)),
                ('area', models.DecimalField(decimal_places=1, max_digits=5)),
                ('room_count', models.IntegerField(default=1)),
                ('floor', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('address', models.CharField(max_length=255)),
                ('deal', models.CharField(choices=[('rent', 'Rent'), ('purchase', 'Purchase')], max_length=15)),
                ('price', models.DecimalField(decimal_places=0, max_digits=8)),
                ('description', models.TextField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='property.owner')),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
        ),
    ]
