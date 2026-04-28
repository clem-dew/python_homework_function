def complete_list(letter, letters_list):
    i = -1

    for char in letters_list:
        if letters_list[i] == ".":
            letters_list[i] = letter
            i -= 1
            print(letters_list)
        else:
            i -= 1
    return letters_list

complete_list("X", letters_list = ["a", "b", "c", ".", "e", ".", "g"])
complete_list("X", letters_list = [".", ".", ".", ".", ".", ".", "."])
