def get_zodiac_signs():
    birth_month = int(input("Type your birth month: "))
    if birth_month < 1 or birth_month > 12:
        print("Error - The month index provided is not valid. Choose between 1 and 12.")
    else:
        zodiac_traits = (
            ("Earth","Capricorn","Leafeon"),
            ("Air","Aquarius","Jolteon"),
            ("Water","Pisces","Vaporeon"),
            ("Fire","Aries","Flareon"),
            ("Earth","Taurus","Leafeon"),
            ("Air","Gemini","Jolteon"),
            ("Water","Cancer","Vaporeon"),
            ("Fire","Leo","Flareon"),
            ("Earth","Virgo","Leafeon"),
            ("Air","Libra","Jolteon"),
            ("Water","Scorpio","Vaporeon"),
            ("Fire","Sagittarius","Flareon")
        )
        zodiac_index = zodiac_traits[birth_month-1]
        user_element = zodiac_index[0]
        zodiac_sign = zodiac_index[1]
        user_eeveelution = zodiac_index[2]
        print(f"Zodiac sign: {zodiac_sign}\nElement: {user_element}\nEeveelution: {user_eeveelution}")

get_zodiac_signs()
