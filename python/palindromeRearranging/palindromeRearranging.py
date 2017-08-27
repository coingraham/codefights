def palindromeRearranging(inputString):
    input_array = list(inputString)
    once = False
    checked_letters = []

    for letter in input_array:
        if letter in checked_letters:
            continue

        if inputString.count(letter) % 2 == 1:
            if once:
                return False
            else:
                once = True
                checked_letters.append(letter)

    return True


if __name__ == '__main__':
    print palindromeRearranging("zyyzzzzz")