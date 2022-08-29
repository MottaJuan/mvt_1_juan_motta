# Generated by Django 4.1 on 2022-08-29 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('fecha_nacimiento', models.DateField()),
                ('numero_fav', models.IntegerField()),
                ('banda_fav', models.CharField(max_length=128)),
            ],
        ),
    ]
