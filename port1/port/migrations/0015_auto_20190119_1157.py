# Generated by Django 2.1.4 on 2019-01-19 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0014_auto_20190119_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='firstname',
            field=models.CharField(max_length=30),
        ),
    ]
