# Generated by Django 2.2.5 on 2020-04-22 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.BooleanField(choices=[(0, 'Male'), (1, 'Female')], default=0),
        ),
    ]
