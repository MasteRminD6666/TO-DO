# Generated by Django 3.1.7 on 2021-03-30 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20210330_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='name',
        ),
    ]
