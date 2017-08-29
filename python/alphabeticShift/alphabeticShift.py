def alphabeticShift(inputString):

    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    letters = list(inputString)
    newstring = ""

    for letter in letters:
        if letter == "z":
            newstring += "a"
            continue

        newstring += str(alphabet[alphabet.index(letter) + 1])

    return newstring


if __name__ == '__main__':
    print alphabeticShift("crazy")