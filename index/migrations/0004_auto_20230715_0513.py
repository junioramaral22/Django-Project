# Generated by Django 3.2.20 on 2023-07-15 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20230714_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='done',
        ),
        migrations.AlterField(
            model_name='index',
            name='localizacao',
            field=models.TextField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='index',
            name='nome',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='index',
            name='patrimonio',
            field=models.TextField(default='', max_length=10),
        ),
    ]
