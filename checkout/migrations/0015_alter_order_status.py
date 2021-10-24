# Generated by Django 3.2.7 on 2021-10-24 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, default='Submitted', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='checkout.orderstatus'),
        ),
    ]