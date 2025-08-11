import requests

def check_website(name):
    try:
        response = requests.get(f"https://{name}")
        if response.status_code == 404:
            return "Strona nie istnieje."
        elif response.status_code == 200:
            return "Strona istnieje i działa poprawnie."
        else:
            return
    except requests.exceptions.ConnectionError:
        return "Strona nie istnieje."

while True:
    website = str(input("Podaj adres strony do weryfikacji: "))
    print(check_website(website))