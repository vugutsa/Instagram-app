# Generated by Django 3.1.5 on 2021-01-19 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gramm', '0004_auto_20210118_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_name',
            new_name='name',
        ),
    ]
