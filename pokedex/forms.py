from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from pokedex.models import Pokemon

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


class PokemonLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())


class PokemonRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "username"]