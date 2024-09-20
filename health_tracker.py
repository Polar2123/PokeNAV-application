def health_tracker():
    sum = 0
    max = 0
    sum_dev =0
    max_day=""
    least_day =""
    weekday=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturdays"]
    set_day = input("Step count per day: ")
    list_set_day = set_day.split(",")
    leng = len(list_set_day)
    if leng == 7:
        least = int(list_set_day[0])
        for i in range(len(list_set_day)):
            sum +=int(list_set_day[i])

        mean = sum / len(list_set_day)
        for i in range(len(list_set_day)):
            sum_dev +=(int(list_set_day[i]) - mean)**2
        standart_deviation = (sum_dev / len(list_set_day))**0.5
        for i in range(leng):
            if max <= int(list_set_day[i]):
                max = int(list_set_day[i])
                max_day = weekday[i]
            if least >= int(list_set_day[i]):
                least = int(list_set_day[i])
                least_day = weekday[i]
    
        message = f"""
{mean:.2f} + / - {standart_deviation:.2f} per day.
Most active day: {max_day}. Least active day:{least_day}
        """
        print(message)
    else:
        print(f"Error - Invalid input. The program needs 7 numbers; you typed {leng}  numbers.")