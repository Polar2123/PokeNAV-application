def detect_palindrome():
    name_list =[]
    pokemone_name = input("Type your pokemon name:")
    for i in range(len(pokemone_name)):
        name_list.append(pokemone_name[i])
    if pokemone_name[0].lower() == pokemone_name[-1].lower():
        print(f"The name '{pokemone_name}' is a palindrome.")
    else:
        print(f"The name '{pokemone_name}' is not a palindrome.")