import requests

from urllib import response


# Create your views here.
def pokemon_name(request):
    payload = {"limit": 151}
    pokemon_list = []
    response = requests.get("https://pokeapi.co/api/v2/pokemon/", params=payload)
    pokemons = response.json()
    for line in pokemons["results"]:
        pokemon_list.append(line["name"])
    return pokemon_list
