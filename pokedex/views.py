import requests

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from pokedex.models import Pokemon
from pokedex.forms import (
    PokemonListForm,
    PokemonDetailForm,
    CreatePokemonForm,
    UpdatePokemonForm,
    DeletePokemonForm,
    PokemonSearchForm,
    PokemonSearchTypeForm
)


class PokemonLists(View):
    form_class = PokemonListForm
    initial = {"key": "value"}
    template_name = "pokedex/pokemon_list.html"

    def get(self, request, *args, **kwargs):
        pokemon_list = Pokemon.objects.all()
        form = self.form_class(initial=self.initial)
        
        return render(request, self.template_name, {"form": form, "list_of_pokemons": pokemon_list})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("pokedex:pokemon-list"))


class PokemonDetails(View):
    form_class = PokemonDetailForm
    initial = {"key": "value"}
    template_name = "pokedex/pokemon_details.html"

    def get(self, request, id, *args, **kwargs):
        pokemon_id = Pokemon.objects.get(id=id)
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"pokemon_id": pokemon_id})


class CreatePokemon(View):
    form_class = CreatePokemonForm
    initial = {"key": "value"}
    template_name = "pokedex/create_pokemon.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("pokedex:pokemon-dex"))

        return render(self.template_name, {"form": form})


class UpdatePokemon(View):
    form_class = UpdatePokemonForm
    initial = {"key": "value"}
    template_name = "pokedex/update_pokemon.html"

    def get(self, request, id, *args, **kwargs):
        pokemon_id = Pokemon.objects.get(id=id)
        form = self.form_class(initial=self.initial, instance=pokemon_id)
        return render(request, self.template_name, {"form": form})

    def post(self, request, id, *args, **kwargs):
        pokemon_id = Pokemon.objects.get(id=id)
        form = self.form_class(request.POST, instance=pokemon_id)
        if form.is_valid():
            form.save()
            # form.cleaned_data
            return redirect("pokedex:pokemon-list")

        return render(self.template_name, {"form": form})


class DeletePokemon(View):
    form_class = DeletePokemonForm
    initial = {"key": "value"}
    template_name = "pokedex/delete_pokemon.html"

    def get(self, request, id, *args, **kwargs):
        pokemon_id = Pokemon.objects.get(id=id)
        form = self.form_class(initial=self.initial, instance=pokemon_id)
        return render(request, self.template_name, {"form": form})

    def post(self, request, id, *args, **kwargs):
        pokemon_id = Pokemon.objects.get(id=id)
        form = self.form_class(request.POST, instance=pokemon_id)
        if form.is_valid():
            pokemon_id.delete()
            return redirect("pokedex:pokemon-list")


class PokemonSearch(View):
    form_class = PokemonSearchForm,
    initial = {"key": "value"}
    template_name = "pokedex/pokemon_search.html"

    def get(self, request, *args, **kwargs):
        error = False
        if "query" in request.GET:
            query = request.GET["query"]
            if not query:
                error = True
            else:
                pokemons = Pokemon.objects.filter(name__icontains=query)
                return render(
                    request,
                    "pokedex/pokemon_search_result.html",
                    {"pokemons": pokemons, "query": query},
                )
        return render(
            request,
            self.template_name,
            {"error": error},
        )


class PokemonSearchType(View):
    form_class = PokemonSearchTypeForm,
    initial = {"key": "value"}
    template_name = "pokedex/pokemon_search_type.html"

    def get(self, request, *args, **kwargs):
        error = False
        if "query" in request.GET:
            query = request.GET["query"]
            if not query:
                error = True
            else:
                pokemons = Pokemon.objects.filter(type__name__icontains=query)
                return render(
                    request,
                    "pokedex/pokemon_search_type_result.html",
                    {"pokemons": pokemons, "query": query},
                )
        return render(
            request,
            self.template_name,
            {"error": error},
        )


class EvolutionChart(View):
    pass


def pokemon_names(request):
    list_pokemons = []
    if "name" in request.GET:
        name = request.GET["name"]
        payload = {"limit": 151}

        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{name}", params=payload
        )
        pokemons = response.json()
        line = pokemons["name"]

        for i in line:
            # for line in pokemons["results"]:
            # list_pokemons.append(line["name"])
            pokemon_list = Pokemon(
                id=i["id"],
                # names=i["name"],
                # height=i["height"],
                # weight=i["weight"],
            )
            pokemon_list.save()
            list_pokemons = Pokemon.objects.all().order_by("id")

    return render(request, "pokedex/index.html", {"list_of_pokemons": list_pokemons})
