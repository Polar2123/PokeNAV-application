def get_hashtags():
    hastags_list=[]
    text = input("Type your post: ")
    if "#" in text:
        list_text = text.split(" ")
        for i in range(len(list_text)):
            if "#" in list_text[i][0]:
                hashtag_word = list_text[i]
                if hashtag_word not in hastags_list:
                    hastags_list.append(hashtag_word)
        print("Hashtags found:")
        for i in range(len(hastags_list)):
                print(hastags_list[i])
    else:
        print("No hashtags found.\n")
