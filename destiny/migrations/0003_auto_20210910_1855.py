# Generated by Django 3.2.5 on 2021-09-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destiny', '0002_alter_destiny_model_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destiny_model',
            name='long_desc',
        ),
        migrations.RemoveField(
            model_name='destiny_model',
            name='ratings',
        ),
        migrations.RemoveField(
            model_name='destiny_model',
            name='reviews',
        ),
        migrations.AlterField(
            model_name='destiny_model',
            name='short_desc',
            field=models.CharField(max_length=200),
        ),
    ]
