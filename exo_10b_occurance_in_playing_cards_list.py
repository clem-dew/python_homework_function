from random import randint

def random_card(n, VALUES = ["as", 2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi"]):
    random_cards_list = []

    for _ in range(n):
        random_index = randint(0, len(VALUES) - 1)
        random_cards_list.append(VALUES[random_index])
    
    for value in set(random_cards_list):
        counter = random_cards_list.count(value)

        if counter == 5:
            print("Poker")
        elif counter == 4:
            print("Carré")
        elif counter == 3:
            print("Brelan")
        elif counter == 2:
            print("Paire")

    return random_cards_list

print(random_card(6))
