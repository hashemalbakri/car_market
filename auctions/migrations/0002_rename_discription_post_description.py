# Generated by Django 4.1 on 2022-10-07 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='discription',
            new_name='description',
        ),
    ]
