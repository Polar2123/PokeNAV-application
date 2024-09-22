def health_tracker():
    #intilized values
    sum_of_steps = 0
    sum_of_steps_means =0
    max_steps =0
    least_steps =0
    max_active_day=""
    least_active_day =""
    weekday=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    set_day = input("Steps Statistics: ")
    if set_day == "": #if set is empty
        list_set_day= [] #list will be empty
    else:
        list_set_day = set_day.split(",") #else will split into list
    length_of_list_day = len(list_set_day)

    #Check if the user provided exact 7 days
    if length_of_list_day == 7:

        #Calculate the mean(average) steps
        for i in range(len(list_set_day)):
            sum_of_steps +=int(list_set_day[i])

        mean = sum_of_steps / len(list_set_day)
        #Calculate the standart deviation 
        for i in range(len(list_set_day)):
            sum_of_steps_means +=(int(list_set_day[i]) - mean)**2
        std_steps = (sum_of_steps_means / len(list_set_day))**0.5
        #Calculate the max and least active day
        for i in range(length_of_list_day):
            if i == 0:
                max_steps = int(list_set_day[i])
                least_steps = int(list_set_day[i])

            if max_steps <= int(list_set_day[i]):
                max_steps = int(list_set_day[i])
                max_active_day = weekday[i]
            if least_steps >= int(list_set_day[i]):
                least_steps = int(list_set_day[i])
                least_active_day = weekday[i]
        #OUTPUT
        message = f"""{mean:.2f} + / - {std_steps:.2f} per day.
Most active day: {max_active_day}. Least active day: {least_active_day}.
        """
        print(message)
    else:
        #Error message for invalid input
        print(f"Error - Invalid input. The program needs 7 numbers; you typed {length_of_list_day} numbers.")