# Generated by Django 4.0.3 on 2022-04-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_date_alter_event_poo_alter_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='poo',
            field=models.BooleanField(default=False),
        ),
    ]
