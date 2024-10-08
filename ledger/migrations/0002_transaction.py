# Generated by Django 5.1 on 2024-08-30 02:11

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_no', models.CharField(blank=True, max_length=128, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('advance', models.FloatField(default=0)),
                ('bill_amount', models.FloatField(default=0)),
                ('balance', models.FloatField()),
                ('grand_balance', models.FloatField()),
                ('remark', models.CharField(blank=True, max_length=128, null=True)),
                ('created_on', models.DateField(default=django.utils.timezone.now)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.staff')),
            ],
        ),
    ]
