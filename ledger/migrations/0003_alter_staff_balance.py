# Generated by Django 4.2 on 2024-09-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]
