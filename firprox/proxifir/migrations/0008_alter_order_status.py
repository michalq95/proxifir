# Generated by Django 4.0.4 on 2022-05-28 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxifir', '0007_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Przyjete', 'In Progress'), ('outsourcowane', 'Outsourced'), ('komplikacje', 'Complications'), ('wykonane', 'Done'), ('oddane', 'Returned')], default='Przyjete', max_length=15),
        ),
    ]
