# Generated by Django 4.2.2 on 2023-09-07 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-publish_date']},
        ),
    ]
