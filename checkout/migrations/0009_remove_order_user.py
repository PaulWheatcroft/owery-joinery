# Generated by Django 3.2.7 on 2021-10-22 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_alter_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
