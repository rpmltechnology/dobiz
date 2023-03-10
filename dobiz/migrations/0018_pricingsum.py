# Generated by Django 4.1.5 on 2023-03-08 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobiz', '0017_banner_category_benefits_category_closure_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingSum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, null=True)),
                ('heading_text', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity_value', models.CharField(blank=True, max_length=100, null=True)),
                ('mark_pric', models.CharField(blank=True, max_length=100, null=True)),
                ('mark_pric_value', models.CharField(blank=True, max_length=100, null=True)),
                ('dobiz', models.CharField(blank=True, max_length=100, null=True)),
                ('dobiz_value1', models.CharField(blank=True, max_length=100, null=True)),
                ('dobiz_value2', models.CharField(blank=True, max_length=100, null=True)),
                ('gst', models.CharField(blank=True, max_length=100, null=True)),
                ('gst_value', models.CharField(blank=True, max_length=100, null=True)),
                ('save', models.CharField(blank=True, max_length=100, null=True)),
                ('save_value', models.CharField(blank=True, max_length=100, null=True)),
                ('govt', models.CharField(blank=True, max_length=100, null=True)),
                ('govt_value', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
