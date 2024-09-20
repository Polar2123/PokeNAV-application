def find_pokemon_bmi():
    pokemon_height = float(input("Type the pokemon height: "))
    pokemon_weight = float(input("Type the pokemon weight: "))

    if pokemon_height == 0:
        print("Error - Height cannot be 0.")
    elif pokemon_height < 0 and pokemon_weight < 0:
        print("Error - Height and weight must be a positive numbers.")
    elif pokemon_height < 0:
        print("Error - Height must be a positive number.")
    elif pokemon_weight < 0:
        print("Error - Weight must be a positive number.")
    else:
        pokemon_bmi = pokemon_weight / (pokemon_height ** 2)
        if pokemon_bmi < 29:
            print(f"BMI = {pokemon_bmi:.2f}. The pokemon is underweight.")
        elif pokemon_bmi < 53:
            print(f"BMI = {pokemon_bmi:.2f}. The pokemon is healthy.")
        elif pokemon_bmi < 85:
            print(f"BMI = {pokemon_bmi:.2f}. The pokemon is overweight.")
        elif pokemon_bmi >= 85:
            print(f"BMI = {pokemon_bmi:.2f}. The pokemon is obese.")
find_pokemon_bmi()
