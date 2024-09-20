from detect_palindrome import detect_palindrome
from get_hashtags import get_hashtags
from health_tracker import health_tracker
from pokemon_traits import get_pokemon_traits

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
    print(menu)
    user_option = int(input("Type your option:\n"))
    while user_option != 1:
        
        if user_option == 1:
            print("Thank you for playing! See you next time!\n")
        elif user_option == 2:
            get_hashtags()
        elif user_option ==3:
            detect_palindrome()
        elif user_option ==4:
            pass
        elif user_option == 5:
            get_pokemon_traits()
        elif user_option ==6:
            pass
        elif user_option ==7:
            pass
        elif user_option ==8:
            health_tracker()
        else:
            print("Error - Invalid option. Please input a number between 1 and 9.")

        return user_option

if __name__ == '__main__':
    choose_menu()




