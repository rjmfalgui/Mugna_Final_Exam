from django import forms
from django.forms import ModelForm
from pokedex.models import Pokemon
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import get_user_model


class PokemonListForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ["id", "name"]


class PokemonDetailForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'


class CreatePokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'


class UpdatePokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'


class DeletePokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'

class PokemonSearchForm(forms.ModelForm):
    name = forms.CharField(required=False)

class PokemonSearchTypeForm(forms.ModelForm):
    name = forms.CharField(required=False)