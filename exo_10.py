from random import randint

VALUES = ["as", 2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi"]

def random_card_1():
    random_index_1 = randint(0, len(VALUES) - 1)
    random_card_1 = VALUES[random_index_1]

    return random_card_1

def random_card_2(n):
    random_cards_list = []

    for _ in range(n):
        random_index_2 = randint(0, len(VALUES) - 1)
        random_card_2 = VALUES[random_index_2]
        random_cards_list.append(random_card_2)

    return random_cards_list


print(random_card_1())
print(random_card_2(6))