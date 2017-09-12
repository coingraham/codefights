def firstDigit(s):

    return [c for c in s if c.isdigit()][0]


def firstDigit2(inputString):

    # Top Python2 Answer
    return filter(lambda c: c.isdigit(), inputString)[0]

if __name__ == '__main__':
    print firstDigit("var_1__Int")