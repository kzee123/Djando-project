# Generated by Django 3.0.6 on 2020-05-15 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20200516_0235'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='feedback',
            new_name='feedbacks',
        ),
    ]