# Generated by Django 3.2 on 2021-11-04 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0003_alter_filme_avaliacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='data_lancamento',
            field=models.DateField(),
        ),
    ]
