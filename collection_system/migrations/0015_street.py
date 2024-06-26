# Generated by Django 4.2.10 on 2024-04-02 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection_system', '0014_district_remove_customerrequest_picture_ward'),
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=255)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection_system.district')),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection_system.ward')),
            ],
        ),
    ]
