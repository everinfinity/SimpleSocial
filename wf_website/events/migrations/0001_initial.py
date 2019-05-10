# Generated by Django 2.1.7 on 2019-05-10 19:15

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', wagtail.core.fields.RichTextField(blank=True)),
                ('date', models.DateTimeField()),
                ('website', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'events',
            },
            bases=('wagtailcore.page',),
        ),
    ]
