# Generated by Django 4.0.3 on 2022-04-02 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='manager',
        ),
    ]
