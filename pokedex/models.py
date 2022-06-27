from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    type = models.ForeignKey("pokedex.PokemonType", related_name="Types", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemons"

    def __str__(self):
        return f"{self.name}"

       
class PokemonStats(models.Model):
    name = models.CharField(max_length=100)
    effort = models.IntegerField()
    base_stat = models.IntegerField()
    pokemon = models.ForeignKey("pokedex.Pokemon", related_name='pokemonstats', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "PokemonStat"
        verbose_name_plural = "PokemonStats"

    def __str__(self):
        return f"{self.name}"

class PokemonType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "PokemonType"
        verbose_name_plural = "PokemonTypes"

    def __str__(self):
        return f"{self.name}"