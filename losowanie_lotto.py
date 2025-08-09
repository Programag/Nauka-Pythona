import random 

def choose_numbers(amount, total_amount):
    numbers = []
    counter = 0
    while amount > counter:
        number = random.randint(0, total_amount)
        if number in numbers:
            counter -= 1
        else:
            numbers.append(number)
        amount -= 1
    return numbers

numbers_list = choose_numbers(6, 49)
for count, element in enumerate(numbers_list, start=1):
        print(f"{count}. {element}")
