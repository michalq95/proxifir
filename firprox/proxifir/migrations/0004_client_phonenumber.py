# Generated by Django 4.0.4 on 2022-05-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxifir', '0003_alter_order_returndate_alter_order_startdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
