from random import randint

NUMBERS = []

def interger_number(n):
    for _ in range(n):
        NUMBERS.append(randint(1, 6))
    return NUMBERS

print(interger_number(8))