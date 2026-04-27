def letter_in_word(letter, word):
    count = 0

    for char in word:
        if char == letter:
            count += 1

    return count

print(letter_in_word("c", "cacao"))
