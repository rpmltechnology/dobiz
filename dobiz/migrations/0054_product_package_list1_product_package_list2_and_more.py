# Generated by Django 4.2 on 2023-06-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobiz', '0053_product_estimated_delivery_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='package_list1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='package_list2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='package_list3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='package_list4',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='package_list5',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='package_list6',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='package_list7',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='package_type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
