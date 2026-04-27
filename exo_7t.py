from random import randint

def generator_word(n, valid_value = ["a", "i", "l", "n", "o", "r", "s", "t"]):
    generated_word = ""

    for _ in range(n):
        random_index = randint(0, len(valid_value) - 1)
        random_letter = valid_value[random_index]
        generated_word += random_letter
        valid_value.pop(random_index)
        
    return generated_word
    
print(generator_word(6))