# Generated by Django 3.2.7 on 2021-10-22 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_additionaluserdetails_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionaluserdetails',
            options={'verbose_name_plural': 'Additional user details'},
        ),
        migrations.RemoveField(
            model_name='additionaluserdetails',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='additionaluserdetails',
            name='last_name',
        ),
    ]
