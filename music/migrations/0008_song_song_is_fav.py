# Generated by Django 2.1.3 on 2018-12-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_album_album_is_fav'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_is_fav',
            field=models.BooleanField(default=False),
        ),
    ]
