# Generated by Django 5.0.4 on 2024-08-29 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
