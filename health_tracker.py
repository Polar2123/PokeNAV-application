def find_mean(set_steps):
    total_steps = 0
    for step in set_steps:
        total_steps +=step
    mean = total_steps / len(set_steps)
    return mean
    
def find_std(mean,set_steps):
    
    variance_sum = 0
    for steps in set_steps:
        variance_sum +=(steps - mean)**2
    std_steps = (variance_sum/ len(set_steps))**0.5
    return std_steps
def find_active_day(day_count, set_steps):
    max_steps =0
    least_steps =0
    max_active_day=""
    least_active_day =""
    weekdays=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i in range(day_count):
        if i == 0:
            max_steps = set_steps[i]
            least_steps = set_steps[i]

        if max_steps <= set_steps[i]:
            max_steps = set_steps[i]
            max_active_day = weekdays[i]

        if least_steps >= set_steps[i]:
            least_steps = set_steps[i]
            least_active_day = weekdays[i]

    return max_active_day, least_active_day
    
def health_tracker():    
    set_steps =[]

    user_input = input("Steps Statistics: ")
    if user_input == "" or user_input == " ": 
        set_steps= [] 
    else:
        step_strings = user_input.split(",") 
        for steps in step_strings:
            set_steps.append(int(steps))        
        
    day_count = len(set_steps)


    if day_count == 7:

        
        mean=find_mean(set_steps)
        
        std_steps=find_std(mean,set_steps)
        
        max_active_day, least_active_day = find_active_day(day_count, set_steps)
        
        message = f"""{mean:.2f} + / - {std_steps:.2f} per day.
Most active day: {max_active_day}. Least active day: {least_active_day}.
        """
        print(message)
    else:
        print(f"Error - Invalid input. The program needs 7 numbers; you typed {day_count} numbers.")
