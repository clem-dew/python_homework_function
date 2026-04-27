from random import randint

def random_card(n, VALUES = ["as", 2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi"]):
    random_cards_list = []

    for _ in range(n):
        random_index = randint(0, len(VALUES) - 1)
        random_cards_list.append(VALUES[random_index])
    
    counts = {x: random_cards_list.count(x) for x in set(random_cards_list)}

    if 5 in counts.values():
        print("Poker")
    elif 4 in counts.values():
        print("Carré")
    elif 3 in counts.values():
        print("Brelan")
    elif 2 in counts.values():
        print("Paire")

    return random_cards_list

print(random_card(6))

# JE N'AI PAS TROUVE SEULE !
# RECHERCHER DOCU SUR counts/dico !