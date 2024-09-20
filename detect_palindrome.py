def detect_palindrome():
    name_list =[]
    pokemone_name = input("Type your pokemon name:").lower()
    for i in range(len(pokemone_name)):
        name_list.append(pokemone_name[i])
    if pokemone_name[0] == pokemone_name[-1]:
        print(f"The name '{pokemone_name}' is a palindrome")
    else:
        print("bro do you know palindrome means")