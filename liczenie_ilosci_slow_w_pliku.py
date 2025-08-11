def count_words(word):
    with open("koty.txt", "r", encoding="UTF8") as file:
        words_counter = 0
        file.read()
        end = file.tell()
        file.seek(0)
        while True:
            data = file.readline()
            if word in data.lower():
                words_counter += 1
            elif word not in data.lower() and file.tell() == end:
                break
        return words_counter
        
data = count_words("kot")
print(data)
