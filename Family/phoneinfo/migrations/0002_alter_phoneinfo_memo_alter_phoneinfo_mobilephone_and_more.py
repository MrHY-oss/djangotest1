# Generated by Django 4.0.4 on 2022-05-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneinfo',
            name='memo',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='phoneinfo',
            name='mobilephone',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='phoneinfo',
            name='other_contact',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='phoneinfo',
            name='other_contact2',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
