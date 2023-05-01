# Generated by Django 4.1.7 on 2023-04-24 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HireDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobrole', models.CharField(blank=True, max_length=200, null=True)),
                ('jobcategory', models.CharField(blank=True, max_length=200, null=True)),
                ('exp', models.CharField(blank=True, max_length=200, null=True)),
                ('qualification', models.CharField(blank=True, max_length=200, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('postdate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]