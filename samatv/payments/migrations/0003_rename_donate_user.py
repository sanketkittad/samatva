# Generated by Django 4.0.2 on 2022-04-27 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_donate_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Donate',
            new_name='User',
        ),
    ]
