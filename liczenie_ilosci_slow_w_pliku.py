def count_words(word):
    with open("koty.txt", "r", encoding="UTF8") as file:
        words_counter = 0
        while True:
            data = file.readline()
            if word.capitalize() in data or word in data:
                words_counter += 1
            else:
                break
        return words_counter
        
data = count_words("kot")
print(data)
