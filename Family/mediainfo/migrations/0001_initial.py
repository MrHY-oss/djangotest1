# Generated by Django 4.0.4 on 2022-05-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=256)),
                ('account', models.CharField(max_length=64)),
                ('passwd', models.CharField(max_length=64)),
            ],
        ),
    ]