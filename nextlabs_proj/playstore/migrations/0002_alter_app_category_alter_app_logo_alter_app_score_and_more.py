# Generated by Django 4.1 on 2022-08-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='category',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='app',
            name='logo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='app',
            name='score',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='sub_Category',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]