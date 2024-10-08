from detect_palindrome import detect_palindrome
from get_hashtags import get_hashtags
from health_tracker import health_tracker
from pokemon_traits import get_pokemon_traits
from zodiac_signs import get_zodiac_signs
from get_acronym import get_acronym
from pokemon_bmi import find_pokemon_bmi
def choose_menu():
    menu = """
Welcome to the Main Menu. Choose one of the options below:

1. Exit
2. Identify hashtags
3. Detect a palindrome
4. Create an acronym
5. Get Pokemon traits
6. Match zodiac sign and element
7. BMI calculator
8. Fitness and Healt Tracking
        """
    user_option = 2
    
    while user_option != 1:
        print(menu)
        user_option = int(input("Type your option:\n"))
        
        if user_option > 9 or user_option < 1:
            user_option = int(input("Error - Invalid option. Please input a number between 1 and 7.\n"))

        if user_option == 1:
            print("Thank you for playing! See you next time!")
        elif user_option == 2:
            get_hashtags()
        elif user_option ==3:
            detect_palindrome()
        elif user_option ==4:
            get_acronym()
        elif user_option == 5:
            get_pokemon_traits()
        elif user_option ==6:
            get_zodiac_signs()
        elif user_option ==7:
            find_pokemon_bmi()
        elif user_option ==8:
            health_tracker()
 

if __name__ == '__main__':
    choose_menu()




