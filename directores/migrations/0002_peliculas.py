# Generated by Django 4.1.5 on 2023-02-02 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelicula', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('estreno', models.DateField(blank=True, null=True)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directores.director')),
            ],
        ),
    ]
