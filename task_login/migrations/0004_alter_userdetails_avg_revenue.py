# Generated by Django 3.2.5 on 2021-07-09 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_login', '0003_alter_userdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='avg_revenue',
            field=models.FloatField(null=True),
        ),
    ]