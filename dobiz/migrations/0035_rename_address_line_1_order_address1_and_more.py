# Generated by Django 4.1.7 on 2023-03-20 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dobiz', '0034_order_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address_line_1',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_line_2',
            new_name='address2',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_line_3',
            new_name='address3',
        ),
    ]
