# Generated by Django 4.1.3 on 2023-01-28 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobiz', '0011_coupan_order_coupan'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sell_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coupan',
            name='coupan',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
