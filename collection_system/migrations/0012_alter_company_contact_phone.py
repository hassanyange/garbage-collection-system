# Generated by Django 4.1.7 on 2024-04-02 08:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_system', '0011_alter_company_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a 10-digit phone number.')]),
        ),
    ]
