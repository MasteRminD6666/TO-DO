# Generated by Django 3.1.7 on 2021-03-26 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20210323_1829'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Acess_record',
        ),
        migrations.DeleteModel(
            name='webpage',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='name',
        ),
        migrations.AddField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
