# Generated by Django 4.2.10 on 2024-05-02 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_guests_alter_event_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(related_name='events', to='events.guest'),
        ),
    ]
