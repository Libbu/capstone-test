# Generated by Django 4.2.11 on 2024-03-13 15:17

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('session_date_time', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=200)),
                ('max_attendees', models.PositiveIntegerField(default=0, verbose_name='Maximum Attendees')),
                ('approved', models.BooleanField(default=False)),
                ('organiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_organiser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
