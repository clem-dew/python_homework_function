def without_vowel(word):
    VOWEL = ["a", "e", "i", "o", "u", "y"]
    without_vowel_word = ""

    for char in word:
        if char not in VOWEL:
            without_vowel_word += char
            
    return without_vowel_word

print(without_vowel("telegramme"))