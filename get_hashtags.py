def get_hashtags():
    #intilize value
    hastags_list=[]
    #user input
    text = input("Type your post: ")
    #check user input contains #
    if "#" in text[0]:
        list_text = text.split(" ") #split to list
        hashtag_word = list_text[i]
        if hashtag_word not in hastags_list:
            hastags_list.append(hashtag_word)
        print("Hashtags found:")
        for i in range(len(hastags_list)):
                print(hastags_list[i])
    else:
        print("No hashtags found.\n")
