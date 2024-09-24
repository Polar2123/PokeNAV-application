def get_acronym():
    name  = input("Type your Pokemon name: ")
    short = int(input("Type your shortening factor: "))


    abbreviated_name   = ""

    for i in range(short-1, len(name), short):
        abbreviated_name += name[i].upper()



    print(f"Abbreviated name: {abbreviated_name}")
