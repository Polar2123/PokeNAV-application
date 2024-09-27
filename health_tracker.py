def mean_finder(list_set_steps):
    sum_of_steps = 0
    for step in list_set_steps:
        sum_of_steps +=step
    mean = sum_of_steps / len(list_set_steps)
    return mean
    
def std_finder(mean,list_set_steps):
    
    sum_of_steps_means =0
    for steps in list_set_steps:
        sum_of_steps_means +=(steps - mean)**2
        std_steps = (sum_of_steps_means / len(list_set_steps))**0.5
    return std_steps
def active_day(length_of_list_day, list_set_steps):
    max_steps =0
    least_steps =0
    max_active_day=""
    least_active_day =""
    weekday=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i in range(length_of_list_day):
        if i == 0:
            max_steps = list_set_steps[i]
            least_steps = list_set_steps[i]

        if max_steps <= list_set_steps[i]:
            max_steps = list_set_steps[i]
            max_active_day = weekday[i]

        if least_steps >= list_set_steps[i]:
            least_steps = list_set_steps[i]
            least_active_day = weekday[i]

    return max_active_day, least_active_day
    
def health_tracker():    
    list_set_steps =[]

    set_day = input("Steps Statistics: ")
    if set_day == "" or set_day == " ": 
        list_set_steps= [] 
    else:
        list_set_str_day = set_day.split(",") #else will split into list
        for steps in list_set_str_day:
            list_set_steps.append(int(steps))        
        
    length_of_list_day = len(list_set_steps)

    #Check if the user provided exact 7 days
    if length_of_list_day == 7:

        #Calculate the mean(average) steps
        mean=mean_finder(list_set_steps)
        #Calculate the standart deviation 
        std_steps=std_finder(mean,list_set_steps)
        #Calculate the max and least active day
        max_active_day, least_active_day = active_day(length_of_list_day, list_set_steps)
        #OUTPUT
        message = f"""{mean:.2f} + / - {std_steps:.2f} per day.
Most active day: {max_active_day}. Least active day: {least_active_day}.
        """
        print(message)
    else:
        #Error message for invalid input
        print(f"Error - Invalid input. The program needs 7 numbers; you typed {length_of_list_day} numbers.")
