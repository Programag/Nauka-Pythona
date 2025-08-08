import random 

numbers = set({})

def choose_numbers(amount, total_amount):
    global numbers
    for i in range(amount):
        number = random.randint(0, total_amount)
        numbers.add(number)
        print(f"{i + 1}. {number}")

choose_numbers(6, 49)
numbers_list = list(numbers)
print(numbers_list)