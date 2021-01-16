# Generated by Django 3.1.5 on 2021-01-16 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/')),
                ('bio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Images_image', models.ImageField(upload_to='images/')),
                ('caption', models.CharField(max_length=60)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramm.profile')),
            ],
        ),
    ]
