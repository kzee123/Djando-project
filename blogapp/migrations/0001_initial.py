# Generated by Django 3.0.6 on 2020-05-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.CharField(max_length=20)),
                ('date_to', models.CharField(max_length=20)),
                ('room_type', models.CharField(max_length=30)),
                ('adults', models.CharField(max_length=20)),
                ('children', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('cnic', models.CharField(max_length=50)),
                ('method', models.CharField(max_length=50)),
            ],
        ),
    ]