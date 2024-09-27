def get_hashtags():
    hashtags_list=[]
    hashtag=""

    sentence = input("Type your post: ")
    text_list = sentence.split(" ")
    for text in text_list:
        if "#" in text[0] and text not in hashtags_list: 
            hashtags_list.append(text)
    if hashtags_list != []:
        print("Hashtags found:")
        for hashtag in hashtags_list:
                print(hashtag)
    else:
         print("No hashtags found.\n")