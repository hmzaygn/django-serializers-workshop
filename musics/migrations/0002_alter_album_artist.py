# Generated by Django 4.1.4 on 2022-12-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ManyToManyField(related_name='albums', to='musics.artist'),
        ),
    ]
