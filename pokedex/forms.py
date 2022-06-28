from django import forms
from django.forms import ModelForm
from pokedex.models import Pokemon
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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


# class RegistrationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = get_user_model()
#         fields = ["username", "email"]

# class PokemonRegistrationForm(forms.Forms):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)

#     class Meta:
#         model: UserCreationForm
#         fields = '__all__'