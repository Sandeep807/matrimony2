# Generated by Django 3.2.8 on 2021-10-08 10:01

import app.managers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0007_auto_20211008_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverRegistration',
            fields=[
                ('registration_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.registration')),
                ('licence', models.CharField(max_length=20)),
                ('aadhar_card', models.IntegerField()),
                ('pan_card', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='driver')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('app.registration',),
            managers=[
                ('objects', app.managers.UserManager()),
            ],
        ),
    ]
