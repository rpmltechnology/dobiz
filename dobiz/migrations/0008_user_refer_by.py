# Generated by Django 4.1.3 on 2023-01-28 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobiz', '0007_product_gst_product_gst_percent_product_other_cost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='refer_by',
            field=models.EmailField(blank=True, max_length=111, null=True),
        ),
    ]
