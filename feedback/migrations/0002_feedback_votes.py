# Generated by Django 2.2.8 on 2019-12-28 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]