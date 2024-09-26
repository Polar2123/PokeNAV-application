def get_pokemon_traits():
    pokemon_name = input("Type your Pokemon name: ")
    pokemon_type = input("Type your Pokemon type: ").capitalize()
    if pokemon_type.lower() == "water":
        pokemon_strength = "Fire-type"
        pokemon_weakness = "Grass-type"
    elif pokemon_type.lower() == "fire":
        pokemon_strength = "Grass-type"
        pokemon_weakness = "Water-type"
    elif pokemon_type.lower() == "grass":
        pokemon_strength = "Water-type"
        pokemon_weakness = "Fire-type"
    else:
        message = """Error - The Pokemon type provided is not valid. Valid types: Water, fire, grass."""
    message = f"{pokemon_name} is a {pokemon_type}-type pokemon! It is strong against {pokemon_strength} Pokemons and weak against {pokemon_weakness} Pokemons."
    print(message)