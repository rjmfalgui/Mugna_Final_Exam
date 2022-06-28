import requests

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from pokedex.decorators import allowed_users, unauthenticated_user
from pokedex.models import Pokemon
from pokedex.forms import (
    PokemonListForm,
    PokemonDetailForm,
    CreatePokemonForm,
    UpdatePokemonForm,
    DeletePokemonForm,
    PokemonSearchForm,
    PokemonSearchTypeForm,
    PokemonLoginForm,
    PokemonRegistrationForm,
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


@method_decorator(login_required(login_url="pokedex:pokemon-login"), name="dispatch")
@method_decorator(allowed_users(allowed_roles=["admin"]), name="dispatch")
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


@method_decorator(login_required(login_url="pokedex:pokemon-login"), name="dispatch")
@method_decorator(allowed_users(allowed_roles=["admin"]), name="dispatch")
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


@method_decorator(login_required(login_url="pokedex:pokemon-login"), name="dispatch")
@method_decorator(allowed_users(allowed_roles=["admin"]), name="dispatch")
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


class PokemonRegistration(ListView):
    form_class = PokemonRegistrationForm
    initial = {"key": "value"}
    template_name = "pokedex/pokemon_registration.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return redirect("pokedex:pokemon-login")
            else:
                return redirect("pokedex:pokemon-registration")

        return render(request, self.template_name, {"form": form})
            
# @method_decorator(unauthenticated_user, name="dispatch")
class PokemonLogin(ListView):
    form_class = PokemonLoginForm
    initial = {"key": "value"}
    template_name = "pokedex/pokemon_login.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            
            if form.is_valid():
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return render(request, "pokedex/index.html", {"username": username})
                    
                    else:
                        return HttpResponse("Incorrect Username and Password")
        
        else:
            form = PokemonLoginForm()
        
        return render(request, self.template_name,{"form": form})


class PokemonLogout(ListView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("pokedex:pokemon-login"))


# @method_decorator(unauthenticated_user, name="dispatch")
class PokemonHome(ListView):
    def get(self, request, *args, **kwargs):
        return render(request, "pokedex/index.html")
