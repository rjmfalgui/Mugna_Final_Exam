from django.contrib import admin
from django.urls import path, include
from pokedex import views
from pokedex.views import(
    PokemonLists,
    PokemonDetails,
    CreatePokemon,
    PokemonLogin,
    UpdatePokemon,
    DeletePokemon,
    PokemonSearch,
    PokemonSearchType,
)

# from pokedex import views

app_name = "pokedex"

urlpatterns = [
    path("", PokemonLogin.as_view(), name="pokemon-dex"),
    path("pokedex-home", views.pokemon_names, name="pokemon-dex"),
    path("pokemon-list/", PokemonLists.as_view(), name="pokemon-list"),
    path("details/<int:id>/", PokemonDetails.as_view(), name="pokemon-details"),
    path("create-pokemon", CreatePokemon.as_view(), name="create-pokemon"),
    path("update-pokemon/<int:id>/", UpdatePokemon.as_view(), name="update-pokemon"),
    path("delete-pokemon/<int:id>/", DeletePokemon.as_view(), name="delete-pokemon"),
    path("pokemon-search/", PokemonSearch.as_view(), name="pokemon-search"),
    path("pokemon-search-type/", PokemonSearchType.as_view(), name="pokemon-search-type"),
]
