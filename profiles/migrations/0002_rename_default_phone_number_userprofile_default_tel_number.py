# Generated by Django 3.2 on 2021-04-28 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_phone_number',
            new_name='default_tel_number',
        ),
    ]
