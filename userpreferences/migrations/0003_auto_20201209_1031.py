# Generated by Django 3.1.4 on 2020-12-09 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpreferences', '0002_auto_20201209_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreference',
            name='currency',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
