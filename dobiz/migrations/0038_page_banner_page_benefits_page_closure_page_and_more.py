# Generated by Django 4.1.7 on 2023-04-04 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dobiz', '0037_coupan_commissionpaid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagename', models.CharField(blank=True, max_length=200, null=True)),
                ('pagetitle', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='banner',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dobiz.page'),
        ),
        migrations.AddField(
            model_name='benefits',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dobiz.page'),
        ),
        migrations.AddField(
            model_name='closure',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dobiz.page'),
        ),
        migrations.AddField(
            model_name='compliance',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dobiz.page'),
        ),
        migrations.AddField(
            model_name='documentrequired',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dobiz.page'),
        ),
        migrations.AddField(
            model_name='faq',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dobiz.page'),
        ),
        migrations.AddField(
            model_name='incorporationprocess',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dobiz.page'),
        ),
        migrations.AddField(
            model_name='meaning',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dobiz.page'),
        ),
        migrations.AddField(
            model_name='minimumrequirement',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dobiz.page'),
        ),
        migrations.AddField(
            model_name='pricingsum',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dobiz.page'),
        ),
        migrations.AddField(
            model_name='stepwiseprocedure',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dobiz.page'),
        ),
    ]