# Generated by Django 5.0.6 on 2024-06-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_system', '0021_payment_alter_company_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerrequest',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
