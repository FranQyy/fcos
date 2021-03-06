# Generated by Django 2.1.1 on 2018-09-11 10:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcos_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gps_longitute', models.FloatField()),
                ('gps_latitude', models.FloatField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ManyToManyField(blank=True, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.ManyToManyField(blank=True, to='fcos_api.Location'),
        ),
    ]
