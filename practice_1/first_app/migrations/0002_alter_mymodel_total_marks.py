# Generated by Django 5.0.4 on 2024-08-27 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='total_marks',
            field=models.IntegerField(default=0),
        ),
    ]
