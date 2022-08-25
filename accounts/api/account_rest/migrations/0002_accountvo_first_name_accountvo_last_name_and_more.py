# Generated by Django 4.0.3 on 2022-08-23 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='user_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
