# Generated by Django 3.2.15 on 2022-09-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=11, upload_to='moviegallery'),
            preserve_default=False,
        ),
    ]
