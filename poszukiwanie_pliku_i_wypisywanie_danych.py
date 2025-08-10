def print_data(name, file_type = ".txt"):
    try:
        with open(f"{name}{file_type}", "r", encoding="UTF8") as file:
            return file.read()
    except FileNotFoundError:
        return "Taki plik nie istnieje."
    
answer = input("Podaj nazwę pliku do odczytania: ")
data = print_data(answer)
print(data)