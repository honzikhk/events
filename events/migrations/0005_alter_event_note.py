# Generated by Django 4.0.4 on 2022-05-30 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_poo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='note',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
