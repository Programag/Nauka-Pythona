def split_names(database):
    names = []
    for element in database:
        if " " in element:
            place = element.index(" ")
            names.append(element[:place])
    return names

def split_surnames(database):
    surnames = []
    for element in database:
        if " " in element:
            place = element.index(" ")
            surnames.append(element[(place + 1):])
    return surnames

def add_data_to_text_file(file_name, database):
    with open(f"{file_name}.txt", "a+", encoding="UTF8") as file:
        for element in database:
            file.write(element)
            file.write("\n")

with open("imionanazwiska.txt", "r", encoding="UTF8") as file:
    names_and_surnames = file.read().splitlines()
    names = split_names(names_and_surnames)
    surnames = split_surnames(names_and_surnames)
    add_data_to_text_file("imiona", names)
    add_data_to_text_file("nazwiska", surnames)