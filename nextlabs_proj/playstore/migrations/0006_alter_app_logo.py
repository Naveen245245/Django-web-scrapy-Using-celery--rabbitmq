# Generated by Django 4.1 on 2022-08-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playstore', '0005_userprofile_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='logo',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]