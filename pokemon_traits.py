def get_pokemon_traits():
    pokemon_name = input("Type your Pokemon name: ")
    pokemon_type = input("Type your Pokemon type: ").capitalize()
    type_chart = ("Water","Fire","Grass")
    if pokemon_type == type_chart[0]:
        pokemon_strength = type_chart[1]
        pokemon_weakness = type_chart[2]
    elif pokemon_type == type_chart[1]:
        pokemon_strength = type_chart[2]
        pokemon_weakness = type_chart[0]
    elif pokemon_type == type_chart[2]:
        pokemon_strength = type_chart[0]
        pokemon_weakness = type_chart[1]
    if pokemon_type not in type_chart:
        message = """Error - The Pokemon type provided is not valid. Valid types: Water, fire, grass."""
    else:
        message = f"{pokemon_name} is a {pokemon_type}-type pokemon! It is strong against {pokemon_strength}-type Pokemons and weak against {pokemon_weakness}-type Pokemons."
    print(message)