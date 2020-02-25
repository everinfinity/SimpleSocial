# Generated by Django 2.2.9 on 2020-02-25 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0017_magazineissue_issue_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazineissue',
            name='cover_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
