from random import randint

def generator_word():
    LETTERS = ["a", "i", "l", "n", "o", "r", "s", "t"]
    generated_word = ""

    for _ in range(5):
        random_index = randint(0, len(LETTERS) - 1)
        random_letter = LETTERS[random_index]
        generated_word += random_letter
        LETTERS.pop(random_index)
        
    return generated_word
    
print(generator_word())
