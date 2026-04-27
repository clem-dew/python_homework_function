TABLE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]

def sum_numbers(TABLE):
    total = 0
    for line in TABLE:
        for value in line:
            total += value
    print(total)

sum_numbers(TABLE)