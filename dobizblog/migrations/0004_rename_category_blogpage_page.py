# Generated by Django 4.1.7 on 2023-04-10 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dobizblog', '0003_category_blogpage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='category',
            new_name='page',
        ),
    ]