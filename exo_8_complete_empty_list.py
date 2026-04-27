def complete_list(letter, letters_list = ["a", "b", "c", ".", "e", ".", "g"]):
    i = -1

    for char in letters_list:
        if letters_list[i] == ".":
            letters_list[i] = letter
            i -= 1
        else:
            i -= 1
    return letters_list

print(complete_list("X"))

# EMPTY LIST

def complete_list_2(letter, letters_list = [".", ".", ".", ".", ".", ".", "."]):
    i = -1

    for char in letters_list:
            if letters_list[i] == ".":
                letters_list[i] = letter
                i -= 1 
                print(letters_list)
            else:
                i -= 1        

    return letters_list

complete_list_2("X")
