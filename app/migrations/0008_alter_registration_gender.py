# Generated by Django 3.2.8 on 2021-10-08 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211008_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('Select Options', 'Select Options'), ('Male', 'Male'), ('Female', 'Female')], max_length=15),
        ),
    ]
