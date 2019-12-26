# Generated by Django 3.0.1 on 2019-12-26 10:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rental_app', '0003_auto_20191226_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hire_transaction',
            name='bike',
        ),
        migrations.AddField(
            model_name='hire_transaction',
            name='bike',
            field=models.ManyToManyField(to='rental_app.Bike'),
        ),
        migrations.RemoveField(
            model_name='hire_transaction',
            name='user',
        ),
        migrations.AddField(
            model_name='hire_transaction',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
