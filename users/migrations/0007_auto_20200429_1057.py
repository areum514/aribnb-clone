# Generated by Django 2.2.5 on 2020-04-29 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200429_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('W', 'Female')], max_length=1),
        ),
    ]