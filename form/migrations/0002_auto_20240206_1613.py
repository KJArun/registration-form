# Generated by Django 3.2.9 on 2024-02-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responses',
            name='Abstract',
        ),
        migrations.AddField(
            model_name='responses',
            name='Link',
            field=models.CharField(default='', max_length=300),
        ),
    ]
