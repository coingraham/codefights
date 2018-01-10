def chessKnight(cell):
    options = 0

    letter = list(cell)[0]
    number = int(list(cell)[1])

    if letter > "a":
        if 2 < number < 7:
            options += 2
        else:
            options += 1

    if letter > "b":
        if 1 < number < 8:
            options += 2
        else:
            options += 1

    if letter < "h":
        if 2 < number < 7:
            options += 2
        else:
            options += 1

    if letter < "g":
        if 1 < number < 8:
            options += 2
        else:
            options += 1

    return options


if __name__ == '__main__':
    print chessKnight("c2")
