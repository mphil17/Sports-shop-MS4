# Generated by Django 3.2 on 2021-04-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0003_auto_20210413_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='user',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
