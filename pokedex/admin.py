from django.contrib import admin
from pokedex.models import Pokemon, PokemonStats, PokemonType

# from pokedex.models import
# Register your models here.


class PokemonAdmin(admin.ModelAdmin):
    fields = ["id", "name", "height", "weight", "type"]
    search_fields = ["id", "name"]

class PokemonTypeAdmin(admin.ModelAdmin):
    fields = ["name"]
    search_fields = ["name"]

admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonType, PokemonTypeAdmin)
admin.site.register(PokemonStats)