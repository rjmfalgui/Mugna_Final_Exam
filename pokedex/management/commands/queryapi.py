import urllib.request
import json

from django.core.management.base import BaseCommand, CommandError
from requests import request
from pokedex.models import Pokemon
from pokedex.views import pokemon_names


class Command(BaseCommand):
    help = "Update database with https://pokeapi.co/api/v2/pokemon/"
    #poke_url = "https://pokeapi.co/api/v2/pokemon/{name}"

 
    def handle(self, *args, **kwargs):
        payload = {"limit": 151}
        get_api = requests.get("https://pokeapi.co/api/v2/pokemon/", params=payload)
        response = get_api.json()
        all_pokemons = []
        
        # for page in pages:
        #     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/?page={page+1}")
            
        for pokemon in response.pokemon_list:
            new_pokemon = Pokemon(name=pokemon.name)
           
            new_pokemon.save()
        self.stdout.write(self.style.SUCCESS(response.get("results")))