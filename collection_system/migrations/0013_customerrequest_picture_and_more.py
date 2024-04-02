# Generated by Django 4.1.7 on 2024-04-02 08:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_system', '0012_alter_company_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerrequest',
            name='picture',
            field=models.ImageField(default='yange.jpg', upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='customerrequest',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a 10-digit phone number.')]),
        ),
    ]
