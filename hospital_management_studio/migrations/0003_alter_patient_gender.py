# Generated by Django 5.0.3 on 2024-03-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_management_studio', '0002_rename_secial_doctor_special'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
    ]