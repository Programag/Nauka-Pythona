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

def sprawdz_liste(slownik, imie, slowo_kluczowe):
    sprawdzacz = [element == slowo_kluczowe for element in slownik[imie]["Doświadczenie"]]
    print(sprawdzacz)
    if any(sprawdzacz):
        return f"{imie} ma '{slowo_kluczowe}' w spisie doświadczeń."
    return f"{imie} nie ma '{slowo_kluczowe}' w spisie doświadczeń."

print(sprawdz_liste(dane, "Jakub", "Java"))
print(sprawdz_liste(dane, "Maria", "C++"))
