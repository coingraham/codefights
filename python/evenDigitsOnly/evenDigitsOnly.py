def evenDigitsOnly(n):

    for i in str(n):
        if int(i) % 2 != 0:
            return False

    return True


if __name__ == '__main__':
    print evenDigitsOnly(248622)