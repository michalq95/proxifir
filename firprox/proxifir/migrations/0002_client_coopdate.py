# Generated by Django 4.0.4 on 2022-05-25 19:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proxifir', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='coopDate',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 25, 19, 35, 16, 863618, tzinfo=utc)),
            preserve_default=False,
        ),
    ]