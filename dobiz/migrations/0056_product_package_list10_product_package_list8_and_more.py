# Generated by Django 4.2 on 2023-06-06 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobiz', '0055_alter_product_package_list1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='package_list10',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='package_list8',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='package_list9',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
