def main():
    get_pokemon_traits()


def get_pokemon_traits():
    pokemon_name = input("Type your Pokemon name: ")
    pokemon_type = input("Type your Pokemon type: ")

    if pokemon_type.lower() == "water":
        message = f"""{pokemon_name} is a Water-type pokemon! It is strong against Fire-type pokemon and weak against Grass-type pokemon.
"""
    elif pokemon_type.lower() == "fire":
        message = f"""{pokemon_name} is a Fire-type pokemon! It is strong against Grass-type pokemon and weak against Water-type pokemon.
"""
    elif pokemon_type.lower() == "grass":
        message = f"""{pokemon_name} is a Grass-type pokemon! It is strong against Water-type pokemon and weak against Fire-type pokemon.
"""
    else:
        message = """Error - The Pokemon type provided is not valid. Valid types: Water, fire, grass."""
    print(message)

if __name__ == "__main__":
    main()
