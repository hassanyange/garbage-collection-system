# Generated by Django 5.0.6 on 2024-06-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_system', '0022_customerrequest_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrequest',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=500.0, max_digits=10),
        ),
    ]