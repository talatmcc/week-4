# Generated by Django 5.0.4 on 2024-08-27 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('name', models.CharField(default='Unknown', max_length=100)),
                ('roll', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('father_name', models.CharField(default='Unknown', max_length=100)),
                ('total_marks', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('father_name', models.CharField(max_length=100)),
            ],
        ),
    ]
