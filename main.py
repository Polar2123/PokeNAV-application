
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
def get_hashtags():
    hastags_list=[]
    text = input("Type your your post: ")
    list_text = text.split(" ")
    for i in range(len(list_text)):
        if "#" in list_text[i]:
            hashtag = list_text[i]
            if hashtag not in hastags_list:
                hastags_list.append(hashtag)
    print("Hashtags Found: ")
    for i in range(len(hastags_list)):
            print(hastags_list[i])
            


    


def choose_menu():
    menu = """
        Welcome to the Main Menu. Choose on of the options below:
            1.Exit
            2.Identify hashtags
            3.Detect a palindrome
            4.Create an acronym
            5.Match zodiac sign and element
            6.Get Pokemon traits
            7.BMI calculator
        """
    print(menu)
    user_option = int(input("Type your option:"))
    while user_option != 1:
        
        if user_option == 1:
            print("Thank you for playing! See you next time!")
        elif user_option == 2:
            get_hashtags()
        
        elif user_option == 5:
            get_pokemon_traits()

        return user_option

if __name__ == '__main__':
    choose_menu()




