# Generated by Django 3.2.5 on 2021-07-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_login', '0007_auto_20210709_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='avg_revenue',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='brand',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='client_type',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='company_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
