# Generated by Django 3.0.3 on 2020-04-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekinoback', '0005_auto_20200331_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(default='null', max_length=63, verbose_name='Номер в базі imdb'),
        ),
    ]
