# Generated by Django 3.2.8 on 2021-10-08 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('source_address', models.TextField()),
                ('destination_address', models.TextField()),
                ('booking_date', models.DateField(blank=True, null=True)),
                ('booking_time', models.TimeField()),
                ('type_vehicle', models.CharField(choices=[('Select Options', 'Select Options'), ('TOYOTA ETIOS', 'TOYOTA ETIOS'), ('SWIFT DZIRE', 'SWIFT DZIRE'), ('MAHINDRA VERITO', 'MAHINDRA VERITO'), ('INNOVA 6+1', 'INNOVA 6+1'), ('INNOVA 7+1', 'INNOVA 7+1'), ('TEMPO TRAVELLER', 'TEMPO TRAVELLER'), ('MINI BUS', 'MINI BUS'), ('SEDAN', 'SEDAN'), ('HATCHBACK', 'HATCHBACK')], max_length=100)),
                ('is_cancel', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False)),
                ('oder_id', models.CharField(max_length=100)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi.booking')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
