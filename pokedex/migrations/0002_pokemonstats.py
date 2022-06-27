# Generated by Django 4.0.5 on 2022-06-27 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('effort', models.IntegerField()),
                ('base_stat', models.IntegerField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemonstats', to='pokedex.pokemon')),
            ],
        ),
    ]