# Generated by Django 4.1.7 on 2023-04-24 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dobizhire', '0002_applyjobs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ApplyJobs',
            new_name='AppliedForJobs',
        ),
        migrations.RenameModel(
            old_name='HireDetails',
            new_name='PostJobs',
        ),
    ]