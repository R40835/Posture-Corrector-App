# Generated by Django 4.1.6 on 2023-04-15 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_feedback_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poorpostures',
            name='state',
        ),
    ]
