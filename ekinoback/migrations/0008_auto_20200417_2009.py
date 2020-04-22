# Generated by Django 3.0.3 on 2020-04-17 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekinoback', '0007_auto_20200417_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='studio',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='назва'),
        ),
    ]