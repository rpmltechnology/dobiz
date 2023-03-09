# Generated by Django 4.1.5 on 2023-03-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobiz', '0015_alter_contact_comment_alter_contact_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(blank=True, max_length=100, null=True)),
                ('review_rating', models.CharField(blank=True, max_length=100, null=True)),
                ('review', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('text2', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text2', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text3', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text4', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('text2', models.TextField(blank=True, null=True)),
                ('text3', models.TextField(blank=True, null=True)),
                ('text4', models.TextField(blank=True, null=True)),
                ('text5', models.TextField(blank=True, null=True)),
                ('text6', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('colorcode1', models.CharField(blank=True, default='#90cd26', max_length=100, null=True)),
                ('colorcode2', models.CharField(blank=True, default='#1742fd', max_length=100, null=True)),
                ('list1', models.CharField(blank=True, max_length=100, null=True)),
                ('list2', models.CharField(blank=True, max_length=100, null=True)),
                ('list3', models.CharField(blank=True, max_length=100, null=True)),
                ('list4', models.CharField(blank=True, max_length=100, null=True)),
                ('list5', models.CharField(blank=True, max_length=100, null=True)),
                ('list6', models.CharField(blank=True, max_length=100, null=True)),
                ('list7', models.CharField(blank=True, max_length=100, null=True)),
                ('list8', models.CharField(blank=True, max_length=100, null=True)),
                ('list9', models.CharField(blank=True, max_length=100, null=True)),
                ('list10', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Closure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text2', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text3', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text4', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('text2', models.TextField(blank=True, null=True)),
                ('text3', models.TextField(blank=True, null=True)),
                ('text4', models.TextField(blank=True, null=True)),
                ('text5', models.TextField(blank=True, null=True)),
                ('text6', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('colorcode1', models.CharField(blank=True, default='#90cd26', max_length=100, null=True)),
                ('colorcode2', models.CharField(blank=True, default='#1742fd', max_length=100, null=True)),
                ('list1', models.CharField(blank=True, max_length=100, null=True)),
                ('list2', models.CharField(blank=True, max_length=100, null=True)),
                ('list3', models.CharField(blank=True, max_length=100, null=True)),
                ('list4', models.CharField(blank=True, max_length=100, null=True)),
                ('list5', models.CharField(blank=True, max_length=100, null=True)),
                ('list6', models.CharField(blank=True, max_length=100, null=True)),
                ('list7', models.CharField(blank=True, max_length=100, null=True)),
                ('list8', models.CharField(blank=True, max_length=100, null=True)),
                ('list9', models.CharField(blank=True, max_length=100, null=True)),
                ('list10', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compliance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text2', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text3', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text4', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('text2', models.TextField(blank=True, null=True)),
                ('text3', models.TextField(blank=True, null=True)),
                ('text4', models.TextField(blank=True, null=True)),
                ('text5', models.TextField(blank=True, null=True)),
                ('text6', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('colorcode1', models.CharField(blank=True, default='#90cd26', max_length=100, null=True)),
                ('colorcode2', models.CharField(blank=True, default='#1742fd', max_length=100, null=True)),
                ('list1', models.CharField(blank=True, max_length=100, null=True)),
                ('list2', models.CharField(blank=True, max_length=100, null=True)),
                ('list3', models.CharField(blank=True, max_length=100, null=True)),
                ('list4', models.CharField(blank=True, max_length=100, null=True)),
                ('list5', models.CharField(blank=True, max_length=100, null=True)),
                ('list6', models.CharField(blank=True, max_length=100, null=True)),
                ('list7', models.CharField(blank=True, max_length=100, null=True)),
                ('list8', models.CharField(blank=True, max_length=100, null=True)),
                ('list9', models.CharField(blank=True, max_length=100, null=True)),
                ('list10', models.CharField(blank=True, max_length=100, null=True)),
                ('list11', models.CharField(blank=True, max_length=100, null=True)),
                ('list12', models.CharField(blank=True, max_length=100, null=True)),
                ('list13', models.CharField(blank=True, max_length=100, null=True)),
                ('list14', models.CharField(blank=True, max_length=100, null=True)),
                ('list15', models.CharField(blank=True, max_length=100, null=True)),
                ('list16', models.CharField(blank=True, max_length=100, null=True)),
                ('list17', models.CharField(blank=True, max_length=100, null=True)),
                ('list18', models.CharField(blank=True, max_length=100, null=True)),
                ('list19', models.CharField(blank=True, max_length=100, null=True)),
                ('list20', models.CharField(blank=True, max_length=100, null=True)),
                ('list21', models.CharField(blank=True, max_length=100, null=True)),
                ('list22', models.CharField(blank=True, max_length=100, null=True)),
                ('list23', models.CharField(blank=True, max_length=100, null=True)),
                ('list24', models.CharField(blank=True, max_length=100, null=True)),
                ('list25', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentRequired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text2', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text3', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text4', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('text2', models.TextField(blank=True, null=True)),
                ('text3', models.TextField(blank=True, null=True)),
                ('text4', models.TextField(blank=True, null=True)),
                ('text5', models.TextField(blank=True, null=True)),
                ('text6', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('colorcode1', models.CharField(blank=True, default='#90cd26', max_length=100, null=True)),
                ('colorcode2', models.CharField(blank=True, default='#1742fd', max_length=100, null=True)),
                ('list1', models.CharField(blank=True, max_length=100, null=True)),
                ('list2', models.CharField(blank=True, max_length=100, null=True)),
                ('list3', models.CharField(blank=True, max_length=100, null=True)),
                ('list4', models.CharField(blank=True, max_length=100, null=True)),
                ('list5', models.CharField(blank=True, max_length=100, null=True)),
                ('list6', models.CharField(blank=True, max_length=100, null=True)),
                ('list7', models.CharField(blank=True, max_length=100, null=True)),
                ('list8', models.CharField(blank=True, max_length=100, null=True)),
                ('list9', models.CharField(blank=True, max_length=100, null=True)),
                ('list10', models.CharField(blank=True, max_length=100, null=True)),
                ('list11', models.CharField(blank=True, max_length=100, null=True)),
                ('list12', models.CharField(blank=True, max_length=100, null=True)),
                ('list13', models.CharField(blank=True, max_length=100, null=True)),
                ('list14', models.CharField(blank=True, max_length=100, null=True)),
                ('list15', models.CharField(blank=True, max_length=100, null=True)),
                ('list16', models.CharField(blank=True, max_length=100, null=True)),
                ('list17', models.CharField(blank=True, max_length=100, null=True)),
                ('list18', models.CharField(blank=True, max_length=100, null=True)),
                ('list19', models.CharField(blank=True, max_length=100, null=True)),
                ('list20', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(blank=True, max_length=100, null=True)),
                ('answer1', models.TextField(blank=True, null=True)),
                ('question2', models.CharField(blank=True, max_length=100, null=True)),
                ('answer2', models.TextField(blank=True, null=True)),
                ('question3', models.CharField(blank=True, max_length=100, null=True)),
                ('answer3', models.TextField(blank=True, null=True)),
                ('question4', models.CharField(blank=True, max_length=100, null=True)),
                ('answer4', models.TextField(blank=True, null=True)),
                ('question5', models.CharField(blank=True, max_length=100, null=True)),
                ('answer5', models.TextField(blank=True, null=True)),
                ('question6', models.CharField(blank=True, max_length=100, null=True)),
                ('answer6', models.TextField(blank=True, null=True)),
                ('question7', models.CharField(blank=True, max_length=100, null=True)),
                ('answer7', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IncorporationProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text2', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text3', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text4', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('text2', models.TextField(blank=True, null=True)),
                ('text3', models.TextField(blank=True, null=True)),
                ('text4', models.TextField(blank=True, null=True)),
                ('text5', models.TextField(blank=True, null=True)),
                ('text6', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('colorcode1', models.CharField(blank=True, default='#90cd26', max_length=100, null=True)),
                ('colorcode2', models.CharField(blank=True, default='#1742fd', max_length=100, null=True)),
                ('list1', models.CharField(blank=True, max_length=100, null=True)),
                ('list2', models.CharField(blank=True, max_length=100, null=True)),
                ('list3', models.CharField(blank=True, max_length=100, null=True)),
                ('list4', models.CharField(blank=True, max_length=100, null=True)),
                ('list5', models.CharField(blank=True, max_length=100, null=True)),
                ('list6', models.CharField(blank=True, max_length=100, null=True)),
                ('list7', models.CharField(blank=True, max_length=100, null=True)),
                ('list8', models.CharField(blank=True, max_length=100, null=True)),
                ('list9', models.CharField(blank=True, max_length=100, null=True)),
                ('list10', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text2', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text3', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text4', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('text2', models.TextField(blank=True, null=True)),
                ('text3', models.TextField(blank=True, null=True)),
                ('text4', models.TextField(blank=True, null=True)),
                ('text5', models.TextField(blank=True, null=True)),
                ('text6', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('colorcode1', models.CharField(blank=True, default='#90cd26', max_length=100, null=True)),
                ('colorcode2', models.CharField(blank=True, default='#1742fd', max_length=100, null=True)),
                ('list1', models.CharField(blank=True, max_length=100, null=True)),
                ('list2', models.CharField(blank=True, max_length=100, null=True)),
                ('list3', models.CharField(blank=True, max_length=100, null=True)),
                ('list4', models.CharField(blank=True, max_length=100, null=True)),
                ('list5', models.CharField(blank=True, max_length=100, null=True)),
                ('list6', models.CharField(blank=True, max_length=100, null=True)),
                ('list7', models.CharField(blank=True, max_length=100, null=True)),
                ('list8', models.CharField(blank=True, max_length=100, null=True)),
                ('list9', models.CharField(blank=True, max_length=100, null=True)),
                ('list10', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MinimumRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text2', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text3', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text4', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('text2', models.TextField(blank=True, null=True)),
                ('text3', models.TextField(blank=True, null=True)),
                ('text4', models.TextField(blank=True, null=True)),
                ('text5', models.TextField(blank=True, null=True)),
                ('text6', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('colorcode1', models.CharField(blank=True, default='#90cd26', max_length=100, null=True)),
                ('colorcode2', models.CharField(blank=True, default='#1742fd', max_length=100, null=True)),
                ('list1', models.CharField(blank=True, max_length=100, null=True)),
                ('list2', models.CharField(blank=True, max_length=100, null=True)),
                ('list3', models.CharField(blank=True, max_length=100, null=True)),
                ('list4', models.CharField(blank=True, max_length=100, null=True)),
                ('list5', models.CharField(blank=True, max_length=100, null=True)),
                ('list6', models.CharField(blank=True, max_length=100, null=True)),
                ('list7', models.CharField(blank=True, max_length=100, null=True)),
                ('list8', models.CharField(blank=True, max_length=100, null=True)),
                ('list9', models.CharField(blank=True, max_length=100, null=True)),
                ('list10', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StepWiseProcedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_text2', models.CharField(blank=True, max_length=100, null=True)),
                ('step1', models.CharField(blank=True, max_length=100, null=True)),
                ('answer1', models.TextField(blank=True, null=True)),
                ('step2', models.CharField(blank=True, max_length=100, null=True)),
                ('answer2', models.TextField(blank=True, null=True)),
                ('step3', models.CharField(blank=True, max_length=100, null=True)),
                ('answer3', models.TextField(blank=True, null=True)),
                ('step4', models.CharField(blank=True, max_length=100, null=True)),
                ('answer4', models.TextField(blank=True, null=True)),
                ('step5', models.CharField(blank=True, max_length=100, null=True)),
                ('answer5', models.TextField(blank=True, null=True)),
                ('step6', models.CharField(blank=True, max_length=100, null=True)),
                ('answer6', models.TextField(blank=True, null=True)),
                ('step7', models.CharField(blank=True, max_length=100, null=True)),
                ('answer7', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
