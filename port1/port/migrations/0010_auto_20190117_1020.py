# Generated by Django 2.1.4 on 2019-01-17 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0009_auto_20190116_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='port',
            old_name='_12th_percentage',
            new_name='tpercentage',
        ),
        migrations.RemoveField(
            model_name='port',
            name='image',
        ),
    ]
