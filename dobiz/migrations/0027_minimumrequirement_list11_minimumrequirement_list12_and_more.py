# Generated by Django 4.1.5 on 2023-03-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobiz', '0026_faq_list11_faq_list12_faq_list13_faq_list14_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='minimumrequirement',
            name='list11',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='minimumrequirement',
            name='list12',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='minimumrequirement',
            name='list13',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
