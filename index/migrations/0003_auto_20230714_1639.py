# Generated by Django 3.2.20 on 2023-07-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20230713_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='description',
            new_name='localizacao',
        ),
        migrations.RenameField(
            model_name='index',
            old_name='title',
            new_name='nome',
        ),
        migrations.AddField(
            model_name='index',
            name='patrimonio',
            field=models.TextField(default=''),
        ),
    ]