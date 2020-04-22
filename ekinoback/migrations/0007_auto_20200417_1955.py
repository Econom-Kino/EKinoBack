# Generated by Django 3.0.3 on 2020-04-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekinoback', '0006_movie_imdb_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Назва жанру'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country_production',
            field=models.CharField(max_length=200, null=True, verbose_name='Країна'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(default='null', max_length=63, null=True, verbose_name='Номер в базі imdb'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_link',
            field=models.URLField(null=True, verbose_name='Посилання на постер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(db_index=True, null=True, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='trailer_link',
            field=models.URLField(null=True, verbose_name='Посилання на трейлер'),
        ),
    ]