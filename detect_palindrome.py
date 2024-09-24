def detect_palindrome():
    pokemone_name = input("Type your pokemon name:")
    first_letter = 0
    last_letter =-1
    if pokemone_name[first_letter].lower() == pokemone_name[last_letter].lower():
        print(f"The name '{pokemone_name}' is a palindrome.")
    else:
        print(f"The name '{pokemone_name}' is not a palindrome.")