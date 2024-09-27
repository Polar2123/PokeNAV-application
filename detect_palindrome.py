def detect_palindrome():
    name_list =[]
    pokemon_name = input("Type your pokemon name:")
    name_length = len(pokemon_name)
    name_reverse = ""
    for i in range(name_length, 0, -1):
        name_reverse += pokemon_name[i - 1]
    if name_reverse.lower() == pokemon_name.lower():
        print(f"The name '{pokemon_name}' is a palindrome.")
    else:
        print(f"The name '{pokemon_name}' is not a palindrome.")