# Generated by Django 2.2.5 on 2020-04-29 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200429_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('krw', 'KRW'), ('usb', 'USD')], default='krw', max_length=3, null=True),
        ),
    ]
