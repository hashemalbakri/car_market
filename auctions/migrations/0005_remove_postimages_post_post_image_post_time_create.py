# Generated by Django 4.1 on 2022-10-07 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_color_rename_models_model_alter_post_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimages',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='auctions.postimages'),
        ),
        migrations.AddField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(null=True),
        ),
    ]