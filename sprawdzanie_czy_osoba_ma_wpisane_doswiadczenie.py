dane = {
    "Jakub" : {
        "Wiek" : "15",
        "Doświadczenie" : ["Python", "Java", "C++"]
    },

    "Maria" : {
        "Wiek" : "21",
        "Doświadczenie" : ["Python", "JavaScript", "C#"]
    }
}

def check_list(database, name, key_word):
    checker = [element == key_word for element in database[name]["Doświadczenie"]]
    if any(checker):
        return f"{name} ma '{key_word}' w spisie doświadczeń."
    return f"{name} nie ma '{key_word}' w spisie doświadczeń."

print(check_list(dane, "Jakub", "Java"))
print(check_list(dane, "Maria", "C++"))
