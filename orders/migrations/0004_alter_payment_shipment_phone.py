# Generated by Django 4.2.2 on 2023-10-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_orderdetails_options_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='shipment_phone',
            field=models.CharField(max_length=50),
        ),
    ]