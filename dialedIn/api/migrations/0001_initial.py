# Generated by Django 3.1.6 on 2021-12-27 21:22

import datetime
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
            name='Coffee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffee_name', models.CharField(max_length=30)),
                ('roaster_name', models.CharField(max_length=30)),
                ('roast_level', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Extraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('extraction_length', models.IntegerField()),
                ('mass_in', models.DecimalField(decimal_places=3, max_digits=5)),
                ('mass_out', models.DecimalField(decimal_places=3, max_digits=5)),
                ('notes', models.CharField(max_length=300)),
                ('coffee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.coffee')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
