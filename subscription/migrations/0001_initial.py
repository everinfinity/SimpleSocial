# Generated by Django 2.2.4 on 2019-11-02 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_type', models.CharField(choices=[('print-only-regular-price', 'Print only - regular price - $36'), ('print-only-true-cost', 'Print only - true cost price - $72'), ('pdf-only-regular-price', 'PDF only - regular price - $30'), ('pdf-only-true-cost', 'PDF only - true cost price - $60'), ('print-and-pdf-regular-price', 'Both print and PDF - regular price - $48'), ('print-and-pdf-true-cost', 'Both print and PDF -true cost price - $96')], help_text='Choose the subscription type you would like to receive.', max_length=255)),
                ('subscriber_given_name', models.CharField(blank=True, default='', help_text='Enter the given name for the subscriber.', max_length=255)),
                ('subscriber_family_name', models.CharField(blank=True, default='', help_text='Enter the family name for the subscriber.', max_length=255)),
                ('subscriber_email', models.EmailField(help_text='Provide an email, so we can communicate any issues regarding this subscription.', max_length=254)),
                ('subscriber_street_address', models.CharField(blank=True, default='', help_text='The street address where this subscription should be shipped.', max_length=255)),
                ('subscriber_postal_code', models.CharField(help_text='Postal code for the shipping address.', max_length=16)),
                ('subscriber_po_box_number', models.CharField(blank=True, default='', help_text='P.O. Box, if relevant.', max_length=32)),
                ('subscriber_address_locality', models.CharField(help_text='City for the shipping address.', max_length=255)),
                ('subscriber_address_region', models.CharField(blank=True, default='', help_text='State for the shipping address.', max_length=255)),
                ('subscriber_address_country', models.CharField(default='United States', help_text='Country for shipping.', max_length=255)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('braintree_id', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
