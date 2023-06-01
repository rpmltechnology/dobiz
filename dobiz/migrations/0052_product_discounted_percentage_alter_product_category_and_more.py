# Generated by Django 4.2 on 2023-05-05 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobiz', '0051_rename_is_packed_product_is_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discounted_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]