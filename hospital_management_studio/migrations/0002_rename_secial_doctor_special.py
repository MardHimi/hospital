# Generated by Django 5.0.3 on 2024-03-23 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_management_studio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='secial',
            new_name='special',
        ),
    ]
