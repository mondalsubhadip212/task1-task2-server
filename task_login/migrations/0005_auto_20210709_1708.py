# Generated by Django 3.2.5 on 2021-07-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_login', '0004_alter_userdetails_avg_revenue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='address',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='avg_revenue',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='client_type',
            field=models.CharField(default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='company_name',
            field=models.CharField(default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='phone_number',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
