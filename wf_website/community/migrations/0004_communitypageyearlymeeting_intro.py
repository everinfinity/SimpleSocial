# Generated by Django 2.1.7 on 2019-04-21 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20190421_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitypageyearlymeeting',
            name='intro',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
