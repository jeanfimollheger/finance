# Generated by Django 4.2.15 on 2024-08-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_flux_budget_or_real_flux_category_flux_period_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='multiplier',
            field=models.FloatField(default=1),
        ),
    ]
