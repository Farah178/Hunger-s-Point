# Generated by Django 5.0.2 on 2024-02-14 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HungerPointApp', '0006_userrole_socialmedia_customuser_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='order_date',
            new_name='order_dt',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='order_time',
        ),
    ]
